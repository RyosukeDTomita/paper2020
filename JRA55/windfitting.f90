program windfitting
    implicit none
    integer :: m,la,lo,a,lac,loc,number0,b
    real :: pi,theta,zerolat,zerolong,zerolat75,zerolong75,d,d2,dd,dd2
    real :: gridlat,gridlong,c,c2,xd,yd
    real,dimension(416017) :: lat,long,ew,ns,z,ang,zv,nsc,ewc,zc,angc
    real,dimension(416017) :: latc,longc
    real,dimension(75,115) :: sumew,sumns,sumang,sumz,aveew,avens,aveang,avez,sumzv
    character*120 namein,nameout,path,readfile,outfile,path2
    path = '/home3/tomita/tomitasoturon2020/JRA55/Yearly/'
    path2 = '/home3/tomita/tomitasoturon2020/JRA55/fit/'
    namein = '00.dat'
    nameout = '00fit.dat'
!-------set parameter--------
    pi = 4*atan(1.e0)
    c = (41.e0-34.e0)/(141.e0-131.e0)
    d = 34.e0-131.e0*c
    c2 = c-1
    d2 = 34.e0-131.e0*c2
    theta = -atan(c)
!    zerolong=cos(theta)*131-sin(theta)*34!ito.f x,y=(0,0)
!    zerolat=sin(theta)*131+cos(theta)*34
    zerolong=131!ito.f x,y=(0,0)
    zerolat=34
    zerolat75 = 40!ito.f x,y=(0,75)
    zerolong75 = (40-d2)/c2
    dd = zerolat75-zerolong75*c
    dd2 = 41.e0 - 141.e0*c2
!    xd = (dd2 -d2)/115
!    yd = (dd -d)/75
    gridlong = 6356.752*2*pi/360.e0
    gridlat = gridlong*cos((40.e0/180.e0)*pi)
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
        longc(a)=long(a)-zerolong
        longc(a)=longc(a)*gridlong
        latc(a)=lat(a)-zerolat
        latc(a)=latc(a)*gridlat
!        longc(a)=cos(theta)*long(a)-sin(theta)*lat(a)!spin theta
!        latc(a)=sin(theta)*long(a)+cos(theta)*lat(a)
        ewc(a)=cos(theta)*ew(a)-sin(theta)*ns(a)!spin theta
        nsc(a)=sin(theta)*ew(a)+cos(theta)*ns(a)
        zc(a)=((nsc(a))**2+(ewc(a)**2))**0.5
        angc(a)=atan2(nsc(a),ewc(a))
!        angc(a)=ang(a)-40.e0
    end do
    do la = 1,75,1
        do lo = 1,115,1
            loc=cos(-theta)*lo*10.e0-sin(-theta)*la*10.e0!spin theta
            lac=sin(-theta)*lo*10.e0+cos(-theta)*la*10.e0
            do a = 1,416017,1
                zv(a)=((latc(a)-lac)**2+(longc(a)-loc)**2)**0.5!calculate distance
!                write(*,*)zv(a)
                if (zv(a)<14.5)then
                    sumzv(la,lo)=sumzv(la,lo)+zv(a)
                    sumew(la,lo)=sumew(la,lo)+ewc(a)*zv(a)
                    sumns(la,lo)=sumns(la,lo)+nsc(a)*zv(a)
                    sumang(la,lo)=sumang(la,lo)+angc(a)*zv(a)
                    sumz(la,lo)=sumz(la,lo)+zc(a)*zv(a)
                    !number0 = number0 + 1
                end if
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
            write(111,1001)la,lo,aveew(la,lo),avens(la,lo),avez(la,lo),aveang(la,lo)*180/pi
1001        format(I2,4x,I3,4F9.3)
        end do
    end do
    close(111)
    close(10)
end do
endprogram windfitting
