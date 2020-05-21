FROM python:3.6-alpine

RUN apk --no-cache add python3 \
                       build-base \
                       python3-dev \
					   py3-numpy\
                       # wget dependency
                       openssl \
					   openssl-dev\
                       # dev dependencies
                       git \
                       bash \
                       sudo \
                       py3-pip \
                       # Pillow dependencies
                       jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev
 
RUN /usr/sbin/adduser -D pillow && \
    python -m pip install --upgrade pip && \
    pip install olefile pytest pytest-cov

COPY requirements.txt .
RUN pip install -r requirements.txt