# Pin our tomcat version to something that has not been updated to remove the vulnerability
# https://hub.docker.com/layers/tomcat/library/tomcat/9.0.59-jdk11/images/sha256-383a062a98c70924fb1b1da391a054021b6448f0aa48860ae02f786aa5d4e2ad?context=explore
FROM lunasec/tomcat-9.0.59-jdk11

ADD flag.txt /root
RUN apt update && apt install maven -y

ADD src/ /prototype/src
ADD pom.xml /prototype

#  Build spring app
WORKDIR /prototype/
RUN mvn clean package

#  Deploy to tomcat
RUN mv target/prototype.war /usr/local/tomcat/webapps/

EXPOSE 8080

CMD ["catalina.sh", "run"]
