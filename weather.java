package com.assignment;

public class SwitchClass3 {

	public static void main(String[] args) {
		String str="rainy";
		switch (str) {
		case "hot":
			System.out.println("It's a summer day");
			break;
		case "cold":
			System.out.println("It is colling day");
			break;
		case "rainy":
			System.out.println("Day full of raining");
			break;
		case "winter":
			System.out.println("Winter days");
			break;
		default:
			System.out.println("Not a weather type");	
		}

	}

}
