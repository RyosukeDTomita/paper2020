program ave
  implicit none
  real :: div
  real,dimension(416017) ::lat,long,z,ang
  real,dimension(416017) :: avez,aveang,sumang,sumz
  character*80 namein,nameout,JRAin,dir1
  integer :: n=21,m=12,y,i,j
  dir1='/home/tomita/research2/JRA55/Monthly/'
  namein='199201.dat'
  nameout='/home/tomita/research2/JRA55/Yearly/aa.dat'
  div=1.0/n
  do i=1,m
     sumz=0.0
     sumang=0.0
     DO  y=1992,2012
        write(namein(1:6),'(I4,I2.2)') y,i
        write(*,*)y,i
        JRAin=trim(dir1)//namein
        open(10,file=JRAin)
        read(10,1001)lat,long,z,ang
1001    format(3x,F6.3,F9.3,21x,F6.3,F9.3)
        close(10)
        sumz=sumz+z
        sumang=sumang+ang
     END DO
     write(nameout(37:38),'(I2.2)') i
     avez =sumz*div
     aveang =sumang*div
     open(2,file=nameout)
     write(2,1002)lat,long,avez,aveang
1002     format(F6.3,F9.3,F6.3,F9.3)
     close(2)
  enddo
end program ave
  
     
        
  
  
