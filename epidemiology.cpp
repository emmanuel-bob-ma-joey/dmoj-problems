#include <iostream>
#include <cmath>


int main()
{
        int limit{};
        std::cin>> limit;
        int initial{};
        std::cin>> initial;
        int factor{};
        std::cin>>factor;
        int total{initial};
        int n{0};

        while (total<=limit)
        {
                n+=1;
                total+=initial*pow(factor,n);
        }

        std::cout<<n;
}
