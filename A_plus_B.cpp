#include <iostream>

int main()
{
	int problems{};
	std::cin>> problems;
	int poop{};
	int peep{};
	for (int i = 0; i<problems;i++)
	{
		std::cin>>poop>>peep;
		std::cout<<poop+peep<<'\n';

	}
	return 0;

}
