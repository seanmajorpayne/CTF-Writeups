# PicoCTF 2017 - Level 2 - Meta Find Me

**Category:** Forensics **Points:** 50

**Description:**

> Find the location of the flag in the image: image.jpg. Note: Latitude and longitude 
> values are in degrees with no degree symbols,/direction letters, minutes, seconds, or 
> periods. They should only be digits. The flag is not just a set of coordinates - if you 
> think that, keep looking!

We are looking for GPS information in a file. A quick Google search for GPS coordinates in
an image will return results about exif. We'll quickly find our coordinates using the
command line

```
$ exif image.jpg
EXIF tags in 'image.jpg' ('Motorola' byte order):
--------------------+----------------------------------------------------------
Tag                 |Value
--------------------+----------------------------------------------------------
Orientation         |Top-left
X-Resolution        |72.0000
Y-Resolution        |72.0000
Resolution Unit     |Inch
Software            |Adobe Photoshop CS6 (Windows)
Date and Time       |2016:02:10 11:55:56
Compression         |JPEG compression
X-Resolution        |72
Y-Resolution        |72
Resolution Unit     |Inch
Color Space         |sRGB
Pixel X Dimension   |500
Pixel Y Dimension   |500
Exif Version        |Exif Version 2.1
FlashPixVersion     |FlashPix Version 1.0
GPS Tag Version     |2.3.0.0
Latitude            |11,  0,  0
Longitude           |31,  0,  0
--------------------+----------------------------------------------------------
EXIF data contains a thumbnail (6989 bytes).
```

Now we have our Latitude and Longitude, but our prompt says coordinates are not the
answer. There may be some other data hidden in the image. Let's run file on it:

```
file image.jpg
image.jpg: JPEG image data, Exif standard: [TIFF image data, big-endian, direntries=8, 
orientation=upper-left, xresolution=110, yresolution=118, resolutionunit=2, software=Adobe 
Photoshop CS6 (Windows), datetime=2016:02:10 11:55:56, GPS-Data], comment: ""Your flag is 
flag_2_meta_4_me_<lat>_<lon>_23c1. Now find the GPS coordinates of this image! (", 
progressive, precision 8, 500x500, frames 3
```

Here we can see the image has a comment with the rest of our flag. Once we input the
latitude and longitude, we're good to go!

Flag: flag_2_meta_4_me_11_31_23c1

