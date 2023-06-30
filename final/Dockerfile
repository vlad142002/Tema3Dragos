FROM gcc:latest

COPY . /usr/src/cpp_test

WORKDIR /usr/src/cpp_test

RUN g++ -o Test main.cpp

CMD [ "timeout", "10s" , "./Test" ]