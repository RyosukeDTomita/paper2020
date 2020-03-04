program windfitting
    implicit none
    integer :: m,la,lo,a,la2,lo2,number0,b
    real :: pi,theta,zerolat,zerolong,zerolat75,zerolong75,d,d2,dd,dd2
    real :: gridlat,gridlong,c,c2,xd,yd
    real,dimension(416017) :: lat,long,ew,ns,z,ang,zv
    real,dimension(416017) :: latc,longc
    real,dimension(75,115) :: sumew,sumns,sumang,sumz,aveew,avens,aveang,avez,sumzv
    character*120 namein,nameout,path,readfile,outfile,path2
    path = '/home3/tomita/tomitasoturon2020/JRA55/Yearly/'
    path2 = '/home3/tomita/tomitasoturon2020/JRA55/fit/'
    namein = '00.dat'
    nameout = '00fit.dat'
!-------set parameter--------
    pi = 4*atan(1.e0)
    c = (41-34)/(141-131)
    d = 34-131*c
    c2 = c-1
    d2 = 34-131*c2
    theta = atan(c)
    zerolong=cos(theta)*131-sin(theta)*34!ito.f x,y=(0,0)
    zerolat=sin(theta)*131+cos(theta)*34
    zerolat75 = 40!ito.f x,y=(0,75)
    zerolong75 = (40-d2)/c2
    dd = zerolat75-zerolong75*c
    dd2 = 41 - 141*c2
    xd = (dd2 -d2)/115
    yd = (dd -d)/75
    gridlat = 6356.752/360
    gridlong = gridlat*cos((40/180)*pi)
!*****************************************
! (zerolat75,zerolong75)
!         ↓
!       / *--------------------
!      /  |                   |
!     /   |    japan sea      |
!    y    |                   |
!   /     |                   |
!  /      *--------------------
! /       ↑
! (zerolat,zerolong)
!****************************************
!-------read file-------
do m = 1,12,1
    write(*,*)m
    do la = 1,75,1
        do lo = 1,115,1
            sumew(la,lo)=0.e0
            sumns(la,lo)=0.e0   
            sumang(la,lo)=0.e0   
            sumz(la,lo)=0.e0   
            sumzv(la,lo)=0.e0
        end do     
    end do
    write(namein(1:2),'(I2.2)')m
    write(nameout(1:2),'(I2.2)')m
    readfile = trim(path)//namein
    outfile = trim(path2)//nameout
    open(10,file=readfile)
    do a = 1,416017,1
        read(10,1000)lat(a),long(a),ew(a),ns(a),z(a),ang(a)
1000    format(6F9.3)
        longc(a)=cos(theta)*long(a)-sin(theta)*lat(a)!spin theta
        latc(a)=sin(theta)*long(a)+cos(theta)*lat(a)
        longc(a)=longc(a)-zerolong
        latc(a)=latc(a)-zerolat
        longc(a)=longc(a)*gridlong
        latc(a)=latc(a)*gridlat
    end do
    do la = 1,75,1
        do lo = 1,115,1
            do b = 1,416017,1
                number0 = 0
            end do
            do a = 1,416017,1
                zv(a)=((lat(a)-la*10)**2+(long(a)-lo*10)**2)**0.5!calculate distance
                sumzv(la,lo)=sumzv(la,lo)+zv(a)
                sumew(la,lo)=sumew(la,lo)+ew(a)*zv(a)
                sumns(la,lo)=sumns(la,lo)+ns(a)*zv(a)
                sumang(la,lo)=sumang(la,lo)+ang(a)*zv(a)
                sumz(la,lo)=sumz(la,lo)+z(a)*zv(a)
                    !number0 = number0 + 1
            end do
        end do
    end do
    do la = 1,75,1
        do lo = 1,115,1
            aveew(la,lo)=sumew(la,lo)/sumzv(la,lo)
            avens(la,lo)=sumns(la,lo)/sumzv(la,lo)
            avez(la,lo)=sumz(la,lo)/sumzv(la,lo)
            aveang(la,lo)=sumang(la,lo)/sumzv(la,lo)
        end do
    end do
    open(111,file=outfile)
    do la = 1,75,1
        do lo = 1,115,1
            write(111,*)la,lo,aveew(la,lo),avens(la,lo),avez(la,lo),aveang(la,lo)
!1001        format(6F9.3)
        end do
    end do
    close(111)
    close(10)
end do
endprogram windfitting
