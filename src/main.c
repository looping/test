/*****
  * filename	: main.c
  * function	: The main file of desocode project.
  * create date	:
  * author		: Xu Luping
  */
#include<stdinc.h>
#include<world.h>
/*
 * function : main | main function	
 * args		: 2
 * argv		: int args (number of arg) | char **argv (values of arg)	
 * return	: int 
 */

int main( int args, char **argv )
{
	char cmd = ' ';
	do{
		printf( "Input '0' to start the world: " );
	}while( scanf( "%c", &cmd ) != 1 );
	if( cmd == '0' )
		world_start();
	return 0;
}
//END OF FILE main.c
