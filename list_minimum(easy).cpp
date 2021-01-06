#include<iostream>
int main()
{
	int num{};
	std::cin>> num;
	int peep{};
	std::cin>>peep;

	for (int i=1; i<(num+1);i++)
	{
		std::cout<<i<<" ";
	};
	return 0;
}
