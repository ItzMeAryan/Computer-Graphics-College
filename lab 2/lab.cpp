#include <graphics.h>
#include <conio.h>
int main()
{
    int gd = DETECT, gm;
    char data[] = "C:\\MinGW\\lib\\libbgi.a";
    initgraph(&gd, &gm, data);
    setcolor(WHITE);
    circle(200, 200, 100);
    rectangle(300, 150, 500, 300);
    line(100, 350, 500, 350);
    getch();
    closegraph();
    return 0;
}

// g++ -o lab.exe lab.cpp -lbgi -lgdi32 -lcomdlg32 -luuid -loleaut32 -lole32
