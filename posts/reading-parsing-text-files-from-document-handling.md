---
title: Reading Parsing Text Files From Document Management (fka Document Handling)
date: 2022-12-08T14:52:41.000Z
lastmod: 2022-12-08T14:59:59.000Z
description: When I started my career, I was blown away by how it seemed the world ran on
text files.  Today, even after years of cloud transformation, the world still
seems to run on text files.  CSVs.  Pipe delimited.  Fixed width.  Caret
delimited even.  Whatever.  This post is all about reading files via x++ in
D365.

Row by row 
CommaTextIO used to be a popular class to use in the on-premise days, and it&#x27;s
still viable, however most of the time in D365 we get a file stream as the file
source as opposed 
tags: D365, x++, CSV, Document Management, Document Handling
author: Michael Stashwick
author_url: https://www.d365stuff.co/author/michael/
publisher: D365 Stuff
publisher_url: https://www.d365stuff.co/
---

8 December 2022 / [D365](/tag/d365/)

# Reading Parsing Text Files From Document Management (fka Document Handling)

When I started my career, I was blown away by how it seemed the world ran on
text files. Today, even after years of cloud transformation, the world still
seems to run on text files. CSVs. Pipe delimited. Fixed width. Caret delimited
even. Whatever. This post is all about reading files via x++ in D365.

## Row by row

CommaTextIO used to be a popular class to use in the on-premise days, and it's
still viable, however most of the time in D365 we get a file stream as the
file source as opposed to a file on a local server. Streams can be handled via
CommaTextStreamIO, and the pattern to implement is the same as CommaTextIO:

    
    
        static void readDocuRefCSV(Common _common)
        {
            DocuRef docuRef = DocumentManagement::findAttachmentsForCommon(_common);
            CommaTextStreamIo CommaTextStreamIo;
            container row;
    
            if(docuRef.ValueRecId)
            {
                CommaTextStreamIo = CommaTextStreamIo::constructForRead(DocumentManagement::getAttachmentStream(docuRef));
                CommaTextStreamIo.inFieldDelimiter(',');
                CommaTextStreamIo.inRecordDelimiter('\r\n');
    
                row = CommaTextStreamIo.read();
    
                while(row)
                {
                    //do row by row stuff
                    row = CommaTextStreamIo.read();
                }
    
                CommaTextStreamIo = null;
            }
        }

## Read to end

The other option is to dump the entire file contents into a giant string to do
whatever you want with. In this example we'll use StreamReader which has the
perfect method, ReadToEnd(), for this scenario.

    
    
        static void readDocuRefTxt(Common _common)
        {
            DocuRef docuRef = DocumentManagement::findAttachmentsForCommon(_common);
            System.IO.StreamReader streamReader;
            
            str fileContents;
    
            if(docuRef.ValueRecId)
            {
                streamReader = new System.IO.StreamReader(DocumentManagement::getAttachmentStream(docuRef));
                fileContents = streamReader.ReadToEnd();
    
                //fileContents now has the entire content of the attached file to do stuff with
    
                streamReader.Close();
                streamReader.Dispose();
            }
        }

Ultimately it's always important to understand what's in the file you're
reading – and what you want to do with it -- in order to plan your approach.

![Michael Stashwick](/content/images/size/w100/2019/07/FacePic.jpg)

#### [Michael Stashwick](/author/michael/)

Read [more posts](/author/michael/) by this author.

[Read More](/author/michael/)

