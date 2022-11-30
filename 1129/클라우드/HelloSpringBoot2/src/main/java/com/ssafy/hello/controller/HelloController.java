package com.ssafy.hello.controller;

import java.util.Collections;
import java.util.Map;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
	@GetMapping("/")
	public ResponseEntity<Map> hello() {
		System.out.println("여기 왔니?");
		return new ResponseEntity<Map>(Collections.singletonMap("msg", "Hello World"), HttpStatus.OK);
		
	}
}
