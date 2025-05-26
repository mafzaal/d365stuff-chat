---
title: D365stuff Chat
emoji: 🦀
colorFrom: yellow
colorTo: red
sdk: docker
pinned: false
---

# D365Stuff Chat

A conversational AI interface for the D365Stuff blog, built by [TheDataGuy.pro](https://thedataguy.pro) using the [Let's Talk](https://github.com/mafzaal/lets-talk) framework. This application allows users to interact with the blog's content in a natural, conversational way.

## Features

- 🤖 AI-powered chat interface for D365Stuff blog content
- 🔍 Smart search and retrieval of relevant blog posts
- 💻 Code examples with syntax highlighting
- 🌐 Multi-language support
- 🎨 Dark/Light theme support
- 📤 File upload capabilities
- 🔒 Privacy-focused (no permanent conversation storage)

## Prerequisites

- Python 3.13 or higher
- Docker (optional, for containerized deployment)
- UV package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mafzaal/d365stuff-chat.git
cd d365stuff-chat
```

2. Install dependencies using UV:
```bash
uv sync
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Running the Application

### Local Development

```bash
uv run chainlit run app.py --port 8000
```

### Docker Deployment

```bash
docker build -t d365stuff-chat .
docker run -p 7860:7860 d365stuff-chat
```

## Project Structure

```
.
├── app.py              # Main application entry point
├── prompt.py           # Chat prompt configuration
├── pipeline.py        # Blog data processing pipeline
├── data/             # Blog post data
├── stats/            # Processing statistics
└── .chainlit/        # Chainlit configuration
```

## Configuration

The application can be configured through:

- `.env` file for environment variables
- `.chainlit/config.toml` for UI settings

## Blog Data Processing

The application includes a pipeline for processing blog posts:

```bash
python pipeline.py [--force-recreate] [--data-dir DATA_DIR] [--output-dir OUTPUT_DIR]
```

Options:
- `--force-recreate`: Force recreation of the vector store
- `--data-dir`: Directory containing blog posts
- `--output-dir`: Directory for stats and artifacts
- `--no-chunking`: Process whole documents without chunking
- `--no-save-stats`: Skip saving document statistics

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Built With

- [Chainlit](https://github.com/Chainlit/chainlit) - Chat UI framework
- [LangChain](https://github.com/langchain-ai/langchain) - AI agent framework
- [Let's Talk](https://github.com/mafzaal/lets-talk) - Conversational AI framework by TheDataGuy.pro
- [Docker](https://www.docker.com/) - Containerization

## Acknowledgments

- Built by [TheDataGuy.pro](https://thedataguy.pro) using the [Let's Talk](https://github.com/mafzaal/lets-talk) framework
- Blog content from [D365Stuff](https://www.d365stuff.co)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
