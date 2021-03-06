from faker.providers import BaseProvider

class Provider(BaseProvider):

    applicationMimeTypes = (

        "application/atom+xml", #  Atom feeds
        "application/ecmascript", #  ECMAScript/JavaScript; Defined in RFC 4329 (equivalent to application/javascript but with stricter processing rules)
        "application/EDI-X12", #  EDI X12 data; Defined in RFC 1767
        "application/EDIFACT", #  EDI EDIFACT data; Defined in RFC 1767
        "application/json", #  JavaScript Object Notation JSON; Defined in RFC 4627
        "application/javascript",   #  ECMAScript/JavaScript; Defined in RFC 4329 (equivalent to application/ecmascript
                                    # but with looser processing rules) It is not accepted in IE 8
                                    # or earlier - text/javascript is accepted but it is defined as obsolete in RFC 4329.
                                    # The "type" attribute of the <script> tag in HTML5 is optional and in practice
                                    # omitting the media type of JavaScript programs is the most interoperable
                                    # solution since all browsers have always assumed the correct
                                    # default even before HTML5.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "application/octet-stream", #  Arbitrary binary data.[6] Generally speaking this type identifies files that are not associated with a specific application. Contrary to past assumptions by software packages such as Apache this is not a type that should be applied to unknown files. In such a case, a server or application should not indicate a content type, as it may be incorrect, but rather, should omit the type in order to allow the recipient to guess the type.[7]
        "application/ogg", #  Ogg, a multimedia bitstream container format; Defined in RFC 5334
        "application/pdf", #  Portable Document Format, PDF has been in use for document exchange on the Internet since 1993; Defined in RFC 3778
        "application/postscript", #  PostScript; Defined in RFC 2046
        "application/rdf+xml", #  Resource Description Framework; Defined by RFC 3870
        "application/rss+xml", #  RSS feeds
        "application/soap+xml", #  SOAP; Defined by RFC 3902
        "application/font-woff", #  Web Open Font Format; (candidate recommendation; use application/x-font-woff until standard is official)
        "application/xhtml+xml", #  XHTML; Defined by RFC 3236
        "application/xml-dtd", #  DTD files; Defined by RFC 3023
        "application/xop+xml", # XOP
        "application/zip", #  ZIP archive files; Registered[8]
        "application/gzip", #  Gzip, Defined in RFC 6713
    )

    audioMimeTypes = (
        "audio/basic",              #  mulaw audio at 8 kHz, 1 channel; Defined in RFC 2046
        "audio/L24",                #  24bit Linear PCM audio at 8-48 kHz, 1-N channels; Defined in RFC 3190
        "audio/mp4",                #  MP4 audio
        "audio/mpeg",               #  MP3 or other MPEG audio; Defined in RFC 3003
        "audio/ogg",                #  Ogg Vorbis, Speex, Flac and other audio; Defined in RFC 5334
        "audio/vorbis",             #  Vorbis encoded audio; Defined in RFC 5215
        "audio/vnd.rn-realaudio",   #  RealAudio; Documented in RealPlayer Help[9]
        "audio/vnd.wave",           #  WAV audio; Defined in RFC 2361
        "audio/webm",               #  WebM open media format
    )

    imageMimeTypes = (
        "image/gif", #  GIF image; Defined in RFC 2045 and RFC 2046
        "image/jpeg", #  JPEG JFIF image; Defined in RFC 2045 and RFC 2046
        "image/pjpeg", #  JPEG JFIF image; Associated with Internet Explorer; Listed in ms775147(v=vs.85) - Progressive JPEG, initiated before global browser support for progressive JPEGs (Microsoft and Firefox).
        "image/png", #  Portable Network Graphics; Registered,[10] Defined in RFC 2083
        "image/svg+xml", #  SVG vector image; Defined in SVG Tiny 1.2 Specification Appendix M
        "image/tiff", #  Tag Image File Format (only for Baseline TIFF); Defined in RFC 3302
        "image/vnd.microsoft.icon", #  ICO image; Registered[11]
    )

    messageMimeTypes = (
        "message/http", #  Defined in RFC 2616
        "message/imdn+xml", #  IMDN Instant Message Disposition Notification; Defined in RFC 5438
        "message/partial", #  Email; Defined in RFC 2045 and RFC 2046
        "message/rfc822", #  Email; EML files, MIME files, MHT files, MHTML files; Defined in RFC 2045 and RFC 2046
    )

    modelMimeTypes = (
        "model/example", #  Defined in RFC 4735
        "model/iges", #  IGS files, IGES files; Defined in RFC 2077
        "model/mesh", #  MSH files, MESH files; Defined in RFC 2077, SILO files
        "model/vrml", #  WRL files, VRML files; Defined in RFC 2077
        "model/x3d+binary", #  X3D ISO standard for representing 3D computer graphics, X3DB binary files
        "model/x3d+vrml", #  X3D ISO standard for representing 3D computer graphics, X3DV VRML files
        "model/x3d+xml", #  X3D ISO standard for representing 3D computer graphics, X3D XML files
    )

    multipartMimeTypes = (
        "multipart/mixed", #  MIME Email; Defined in RFC 2045 and RFC 2046
        "multipart/alternative", #  MIME Email; Defined in RFC 2045 and RFC 2046
        "multipart/related", #  MIME Email; Defined in RFC 2387 and used by MHTML (HTML mail)
        "multipart/form-data", #  MIME Webform; Defined in RFC 2388
        "multipart/signed", #  Defined in RFC 1847
        "multipart/encrypted", #  Defined in RFC 1847
    )

    textMimeTypes = (
        "text/cmd", #  commands; subtype resident in Gecko browsers like Firefox 3.5
        "text/css", #  Cascading Style Sheets; Defined in RFC 2318
        "text/csv", #  Comma-separated values; Defined in RFC 4180
        "text/html", #  HTML; Defined in RFC 2854
        "text/javascript", # (Obsolete): JavaScript; Defined in and obsoleted by RFC 4329 in order to discourage its usage in favor of application/javascript. However, text/javascript is allowed in HTML 4 and 5 and, unlike application/javascript, has cross-browser support. The "type" attribute of the <script> tag in HTML5 is optional and there is no need to use it at all since all browsers have always assumed the correct default (even in HTML 4 where it was required by the specification).
        "text/plain", #  Textual data; Defined in RFC 2046 and RFC 3676
        "text/vcard", #  vCard (contact information); Defined in RFC 6350
        "text/xml", #  Extensible Markup Language; Defined in RFC 3023
    )

    videoMimeTypes = (
        "video/mpeg", #  MPEG-1 video with multiplexed audio; Defined in RFC 2045 and RFC 2046
        "video/mp4", #  MP4 video; Defined in RFC 4337
        "video/ogg", #  Ogg Theora or other video (with audio); Defined in RFC 5334
        "video/quicktime", #  QuickTime video; Registered[12]
        "video/webm", #  WebM Matroska-based open media format
        "video/x-matroska", #  Matroska open media format
        "video/x-ms-wmv", #  Windows Media Video; Documented in Microsoft KB 288102
        "video/x-flv", #  Flash video (FLV files)
    )

    mimeTypes = {
        'application':applicationMimeTypes,
        'audio':audioMimeTypes,
        'image':imageMimeTypes,
        'message':messageMimeTypes,
        'model':modelMimeTypes,
        'multipart':multipartMimeTypes,
        'text':textMimeTypes,
        'video':videoMimeTypes
    }

    @classmethod
    def mimeType(cls, type=None):
        """
        :param type: application|audio|image|message|model|multipart|text|video
        """
        type = type if type else cls.randomElement( cls.mimeTypes.keys() )
        return cls.randomElement( cls.mimeTypes[type]  )

