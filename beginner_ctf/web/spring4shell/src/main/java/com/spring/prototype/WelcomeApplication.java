package com.spring.prototype;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;


@SpringBootApplication
public class WelcomeApplication extends SpringBootServletInitializer{
	public static void main(String[] args) {
		SpringApplication.run(WelcomeApplication.class, args);
	}

}
