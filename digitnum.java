package com.assignment;

public class IfClass2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a=99;
		if (a<10) {
			System.out.println("it is one digit number");
		}
		else if (a>=10 & a<100) {
			System.out.println("it is two digit number");
		}
		else if (a>=100 & a<1000) {
			System.out.println("it is three digit number");
		}
		else if (a>=1000 & a<10000) {
			System.out.println("it is four digit number");
		}
		else if (a>=10000 & a<100000) {
			System.out.println("it is five digit number");
		}
		else {
			System.out.println("number is not between 1 & 99999");
		}

	}

}
