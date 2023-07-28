#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - a func that returns
 * Return: o
 */

int infinte_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry pt
 * Return: 0
 */

int main(void)
{
	int child = 0;
	pid_t child_pid;

	while (child < 5)
	{
		child_pid = fork();
		if (!child_pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)child_pid);
		child++;
	}
	if (child_pid != 0)
		infinte_while();
	return (0);
}
