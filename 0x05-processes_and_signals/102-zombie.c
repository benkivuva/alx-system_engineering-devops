#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * create_zombie_processes - Create zombie processes
 *
 * Return: 1 if parent process, 0 if child process
 */
int create_zombie_processes(void)
{
	pid_t pid = 1;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %d\n", pid);
		else
			break;
	}

	if (pid > 0)
		return 1;
	else
		return 0;
}

/**
 * infinite_while - Wait forever
 */
void infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
}

/**
 * main - Create zombie processes
 *
 * Return: 0
 */
int main(void)
{
	pid_t pid = 1;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %d\n", pid);
		else
			break;
	}

	if (pid > 0)
		infinite_while();
	else
		exit(0);

	return 0;
}
