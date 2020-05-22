FROM python:3.6.10-alpine

WORKDIR /tmp

RUN apk --no-cache add gcc\
						musl-dev\
						libc-dev\
						build-base\
						libffi-dev\
						openssl-dev\
						zlib-dev\
						jpeg-dev
						

COPY requirements.txt .

RUN pip3 install --upgrade pip && \
	pip3 install virtualenv && \
	pip3 install --no-cache-dir -r requirements.txt

CMD ["python"]