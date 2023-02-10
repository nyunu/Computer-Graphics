from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class FreeDrawing:
   def __init__(self):
      self.lw = 3.0
      self.color = 'r'
      self.width = 600
      self.height = 600
      self.p1_x = 0
      self.p1_y = 0
      self.p2_x = 0
      self.p2_y = 0
      self.newline=0 # line drawing state (0, 1, 2)
      self.curX = 0
      self.curY = 0

   def MyDisplay(self):
      glLineWidth(self.lw)
      
      if self.color=='r':
         glColor3f(1.0, 0.0, 0.0) # red 색 지정
      elif self.color=='g':
         glColor3f(0.0, 1.0, 0.0) # green 색 지정
      elif self.color == 'b':
         glColor3f(0.0, 0.0, 1.0) # blue 색 지정
      elif self.color == 'c':
         glColor3f(0.0, 1.0, 1.0) # Cyan 색 지정
      elif self.color == 'm':
         glColor3f(1.0, 0.0, 1.0) # Magenta 색 지정
      elif self.color == 'y':
         glColor3f(1.0, 1.0, 0.0) # Yellow 색 지정

      glBegin(GL_LINES)
      glVertex3f(self.p1_x /600, (self.height - self.p1_y) /600, 0.0) # 좌표 정규화
      glVertex3f(self.p2_x /600, (self.height - self.p2_y) /600, 0.0)
      glEnd()
      glFlush()
      
   def MyKeyboard(self, KeyPressed,  X,  Y):

      if KeyPressed==b'q': 
         sys.exit(0)
      elif KeyPressed==b'1': #눌려지는 키보드 버튼에 따라 색지정
         self.color = 'r'
         print(self.color)
      elif KeyPressed==b'2': 
         self.color = 'g'
         print(self.color)
      elif KeyPressed==b'3': 
         self.color = 'b'
         print(self.color)
      elif KeyPressed==b'4': 
         self.color = 'c'
         print(self.color)
      elif KeyPressed==b'5': 
         self.color = 'm'
         print(self.color)
      elif KeyPressed==b'6': 
         self.color = 'y'
         print(self.color)
      elif KeyPressed==GLUT_KEY_DOWN: #눌려지는 키보드 버튼에 따라 두께지정
         self.lw = self.lw - 1.0
         glLineWidth(self.lw)
         print("down line width", self.lw)
      elif KeyPressed==GLUT_KEY_UP : 
         self.lw = self.lw + 1.0
         glLineWidth(self.lw)
         print("up line width", self.lw)
      elif KeyPressed==b'c': 
         self.p1_x = 0
         self.p1_y = 0
         self.p2_x = 0
         self.p2_y = 0
         self.lw = 3.0
         print("Clear Screen")
         glClear(GL_COLOR_BUFFER_BIT)
         glutPostRedisplay()
         
   def MyMouseClick(self, Button, State, X, Y):
      if Button==GLUT_LEFT_BUTTON and State==GLUT_DOWN:
         self.p1_x = X
         self.p1_y = Y
         self.newline = 1   # a line drawing starts
      else:
         self.newline = 0   # a line drawing finishes

   def MyMouseMove(self, X, Y):
      if self.newline == 0: return   # a line drawing finished (not drawing)
      if self.newline == 2:         # a line is being drawing
         # p2 is copied at p1
         self.p1_x = self.p2_x #
         self.p1_y = self.p2_y #
      # if a line starts or continues
      self.p2_x = X   # current mouse point is assigned to p2
      self.p2_y = Y
      self.newline = 2
      glutPostRedisplay()


   def main(self):
      glutInit()
      glutInitDisplayMode(GLUT_RGB) 
      glutInitWindowSize(600, 600)       
      glutCreateWindow("Mouse - callback")
      glMatrixMode(GL_PROJECTION)    
      glLoadIdentity()    
      glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)

      glutDisplayFunc(self.MyDisplay)
      glClear(GL_COLOR_BUFFER_BIT)
      glutKeyboardFunc(self.MyKeyboard) # 숫자키 키보드 콜백함수
      glutSpecialFunc(self.MyKeyboard) #방향키 키보드 콜백함수
      glutMouseFunc(self.MyMouseClick) # 마우스 콜백함수               
      glutMotionFunc(self.MyMouseMove) # 마우스 콜백함수
      glutMainLoop()

d = FreeDrawing()
d.main()