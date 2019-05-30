#include "types.h"
#include "stat.h"
#include "user.h"

int
main(int argc, char *argv[])
{
	int pid1;
	printf(1, "fork_large_mem_test\n");

	char * dummy = (char *) malloc(sizeof(char) * 200 * 1024 * 1024);
	pid1 = fork();
	if(pid1 == 0) {
		printf(1, "I'm child process\n");
		sleep(2);
		exit();
	} else if(pid1 > 0) {
		wait();
		printf(1, "I'm parent process\n");
	} else {
		printf(1, "TEST FAILED\n");
		exit();
	}
	printf(1, "TEST PASSED\n");
	free(dummy);
	exit();
}
