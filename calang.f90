program calang
  implicit none
  real,dimension(8625) :: uab,vab,ang,z,tb,elb,d
  character*120 namein,nameout,POMin,POMout,dir1,nameout2,POMout2,nameout3,POMout3,nameout4,POMout4
  integer,dimension(8625) :: i,j
  real :: pai
  integer ::y,x
  dir1 =  '/home/tomita/model/result/'
  namein = 'BP222_000000_00_00'
  nameout = 'EBP222_000000_00_00' !vector
  nameout2 = 'ABP222_000000_00_00' !temperature
  nameout3 = 'TBP222_000000_00_00' !surface elevation
 ! nameout4 = 'ZBP222_000000_00_00'
!------------- Read Flow speed of U and V-------------
!  do y = 10,8000,10
  do y = 10,4000,10
     write(namein(7:12),'(I6.6)')y
     write(nameout(8:13),'(I6.6)')y
     write(nameout2(8:13),'(I6.6)')y
     write(nameout3(8:13),'(I6.6)')y
!     write(nameout4(8:13),'(I6.6)')y
     POMin = trim(dir1)//namein
     POMout = trim(dir1)//nameout
     POMout2 = trim(dir1)//nameout2
     POMout3 = trim(dir1)//nameout3
!     POMout4 = trim(dir1)//nameout4
     write(*,*)y
     open(10,file=POMin)
     do x = 1,8625
        read(10,1001) i(x),j(x),tb(x),elb(x),uab(x),vab(x),d(x)
1001    format(2I3,F15.5,15x,F15.5,15x,3F15.5,205x)
!        read(10,*)
        !        write(*,*)uab(x),vab(x)
        pai = 4*atan(1.0)
        ang(x) =(180/pai)*atan2(vab(x),uab(x))
        z(x) = SQRT(uab(x)**2+vab(x)**2)
     end do
     close(10)
     open(11,file=POMout)
     open(21,file=POMout2)
     open(31,file=POMout3)
!     open(41,file=POMout4)
     do x = 1,8625
        write(11,1002)i(x),j(x),uab(x),vab(x),z(x),ang(x)
1002    format(2I3,4F15.5)
        write(21,1003)i(x),j(x),tb(x)
        if ((i(x)>2) .and. (j(x)>2) .and. (i(x)<114) .and. (j(x)<74)) then
1003       format(2I3,F15.5)
           write(31,1003)i(x),j(x),d(x)
        end if
        !        write(41,1003)i(x),j(x),zflux(x)
     end do
  end do
  close(11)
  close(21)
  close(31)
  close(41) 
end program calang
  








      
         
         
         
         
          
          
