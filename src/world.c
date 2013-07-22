#include<world.h>
World init_world(void){
	World world;
	return world;
}
void run(World world){
	while(1){
		printf("\nWorld is running!");
	}
}
void world_start(void){
	run(init_world());
}
