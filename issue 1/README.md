你好
------
* 就这样了

	```
	再见
	```
	
	```objective-c
	
	# pragma mark Pragma 

	- (Apple *)eat:(Apple *)apple {
		NSInteger age = apple.age;
		if (age > NSIntegerMax) {
			apple = nil;
		} else {
			age ++;
		}
		self.age = age;
    	return [apple eat:self];
	}
	
	```
	
	
