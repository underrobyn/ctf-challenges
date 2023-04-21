FROM amazoncorretto:17-alpine3.17-jdk

WORKDIR /app

COPY CCEncryptService.java .

RUN javac CCEncryptService.java

RUN mkdir /jar

RUN jar cfe /jar/CCEncryptService.jar CCEncryptService *.class

CMD ["sh"]

