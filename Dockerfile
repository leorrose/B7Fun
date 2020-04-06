FROM python:3.6-alpine

RUN apk --no-cache add python3 \
                       build-base \
                       python3-dev \
                       # wget dependency
                       openssl \
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

ADD depends /depends
RUN cd /depends && ./install_webp.sh && ./install_imagequant.sh && ./install_raqm.sh

RUN /usr/sbin/adduser -D pillow && \
    pip3 install virtualenv && virtualenv /vpy3 && \
    /vpy3/bin/pip install --upgrade pip && \
    /vpy3/bin/pip install olefile pytest pytest-cov && \
    /vpy3/bin/pip install numpy --only-binary=:all: || true && \
    chown -R pillow:pillow /vpy3

COPY ./requirements.txt .
RUN pip install -r requirements.txt

USER pillow
CMD ["depends/test.sh"]