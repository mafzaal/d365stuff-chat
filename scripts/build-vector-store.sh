#!/bin/bash
# Script to build vector store locally
# Usage: ./scripts/build-vector-store.sh [--force-recreate] [--cleanup] [--help]

set -e  # Exit on error

# Default values
OUTPUT_DIR=${OUTPUT_DIR:-"./artifacts"}
DATA_DIR="/home/mafzaal/source/d365stuff/posts/"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="$OUTPUT_DIR/build_${TIMESTAMP}.log"

# Function to display help
show_help() {
    cat << EOF
Usage: ./scripts/build-vector-store.sh [OPTIONS]

Options:
    --force-recreate    Force recreation of the vector store
    --cleanup          Clean up temporary files after build
    --help             Show this help message

Environment variables:
    FORCE_RECREATE     Set to "true" to force recreation of the vector store
    OUTPUT_DIR         Directory to save stats and artifacts (default: ./artifacts)
    USE_CHUNKING       Set to "false" to disable document chunking
    SHOULD_SAVE_STATS  Set to "false" to disable saving document statistics
EOF
    exit 0
}

# Function to log messages
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Function to check if required tools are installed
check_requirements() {
    local missing_tools=()
    
    for tool in uv zip; do
        if ! command -v "$tool" &> /dev/null; then
            missing_tools+=("$tool")
        fi
    done
    
    if [ ${#missing_tools[@]} -ne 0 ]; then
        log "Error: The following required tools are missing: ${missing_tools[*]}"
        exit 1
    fi
}

# Parse command line arguments
FORCE_RECREATE=""
CLEANUP=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --force-recreate)
            FORCE_RECREATE="--force-recreate"
            shift
            ;;
        --cleanup)
            CLEANUP=true
            shift
            ;;
        --help)
            show_help
            ;;
        *)
            log "Error: Unknown option $1"
            show_help
            ;;
    esac
done

# Create output directory and log file
mkdir -p "$OUTPUT_DIR"
touch "$LOG_FILE"

# Check requirements
check_requirements

# Validate data directory
if [ ! -d "$DATA_DIR" ]; then
    log "Error: Data directory '$DATA_DIR' does not exist"
    exit 1
fi

log "Starting vector store build"
log "Output directory: $OUTPUT_DIR"
log "Force recreate: ${FORCE_RECREATE:-false}"
log "Cleanup after build: $CLEANUP"

# Run pipeline in CI mode
log "Running pipeline..."
if ! uv run -m lets_talk.pipeline $FORCE_RECREATE \
    --ci \
    --data-dir "$DATA_DIR" \
    --data-dir-pattern "*.md" \
    --base-url "https://www.d365stuff.co/" \
    --blog-base-url "https://www.d365stuff.co/" \
    --output-dir "$OUTPUT_DIR" \
    --vector-storage-path "$OUTPUT_DIR/vector_store_d365stuff" \
    --collection-name d365stuff_documents; then
    
    log "Error: Pipeline execution failed"
    exit 1
fi

# Check if vector store directory exists and create zip
if [ -d "$OUTPUT_DIR/vector_store_d365stuff" ]; then
    log "Creating vector store zip file..."
    
    cd "$OUTPUT_DIR/vector_store_d365stuff/"
    zip -r "$OUTPUT_DIR/vector_store_${TIMESTAMP}.zip" "$OUTPUT_DIR/vector_store_d365stuff/" 
    log "Vector store zip created at $OUTPUT_DIR/vector_store_${TIMESTAMP}.zip"
    
    

else
    log "Error: Vector store directory not found at $OUTPUT_DIR/vector_store_d365stuff"
    exit 1
fi

# Cleanup if requested
if [ "$CLEANUP" = true ]; then
    log "Cleaning up temporary files..."
    rm -rf "$OUTPUT_DIR/vector_store_d365stuff"
    log "Cleanup completed"
fi

log "Build completed successfully"
log "Artifacts available in $OUTPUT_DIR:"
ls -la "$OUTPUT_DIR" | tee -a "$LOG_FILE"

exit 0
