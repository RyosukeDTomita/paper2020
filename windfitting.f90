program windfitting
    implicit none
    integer :: m,la,lo,a
    real :: pi,theta,zerolat,zerolong,zerolat75,zerolong75,d
    real,dimension(416017)lat,long,ew,ns,z,ang
    real,demension(75*115)sumew,sumns,sumang,sumz,
    character*120 namein,nameout,path,readfile,outfile,path2
    path = '/home3/tomita/tomitasoturon2020/JRA55/Yearly/'
    path2 = '/home3/tomita/tomitasoturon2020/JRA55/'
    namein = '00.dat'
    nameout = '00fit.dat'
!-------set parameter--------
    pi = 4*atan(1)
    theta = (-40/180)*pi
    zerolong=cos(theta)*131-sin(theta)*34!ito.f x,y=(0,0)
    zerolat=sin(theta)*131+cos(theta)*34
    c = (41-34)/(141-131)
    c2 = c-1
    d = 34-131*c2
    zerolat75 = 40!ito.f x,y=(0,75)
    zerolong75 = (40-d)/c2
!-------read file-------
do m = 1,12,1
    write(*,*)m,pi
    do la = 1,75,1
        do lo = 1,115,1
            sumew(la,lo)=0.e0
            sumns(la,lo)=0.e0   
            sumang(la,lo)=0.e0   
            sumz(la,lo)=0.e0   
        end do     
    end do
    write(namein(1:2)'(I2.2)')m
    write(nameout(1:2)'(I2.2)')m
    readfile = trim(path)//namein
    outfile = trim(path2)//nameout
    open(10,file(readfile)
    do a = 1,416017,1
        read(10,1000)lat(a),long(a),ew(a),ns(a),z(a),ang(a)
1000    format(6F9.3)
        if ((lat(a)>31) .and. (long(a)<zerolong75))then
            long(a)=cos(theta)*long(a)-sin(theta)*lat(a)
            lat(a)=sin(theta)*long(a)+cos(theta)*lat(a)
            long(a)=long(a)-zerolong
            lat(a)=lat(a)-zerolat
            
