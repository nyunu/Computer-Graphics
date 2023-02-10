from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class SolarLighting:
    
    MODE_FLAT = 1
    MODE_SMOOTH = 2
    LIGHT_ON = 3
    LIGHT_OFF = 4

    def __init__(self):
    
        self.angle = 0.0
        self.angle2 = 0.0
        self.rotate = 0 # ratateauto 꺼져있는 상태 = 0 / 1이면 켜진거
        self.speed = 35 # 속도 건들지 않아도 됨
        self.depth = 1 
        self.myview = 0 # front view
        self.iShade = SolarLighting.MODE_SMOOTH # 스무드쉐이딩
        self.iLight1 = SolarLighting.LIGHT_OFF # 조명 하나밖에 없음 꺼진상태 !
        self.light0_x = 300 # 조명 좌표
        self.light0_y = 300 
        self.light0_z = 0
        
        self.LIGHT0_lightPos = [self.light0_x, self.light0_y, self.light0_z, 1.0 ] # 실수 #Initial Light position  
        self.LIGHT0_ambient = [0.3, 0.3, 0.3, 1.0 ]
        self.LIGHT0_diffuse = [0.7, 0.7, 0.7, 1.0 ]
        self.LIGHT0_specular = [0.5, 0.5, 0.5, 1.0 ]

        self.ambientLight = [0.1, 0.1, 0.1, 1.0 ] # 전역        
        self.ambient_ref = [0.5, 0.5, 0.5, 1.0 ]
        self.diffuse_ref = [0.7, 0.7, 0.7, 1.0 ]
        self.specular_ref = [1.0, 1.0, 1.0, 1.0 ]

    def menu(self, value):
        
        if value ==1: self.speed = 45
        elif value == 2: self.speed = 35
        elif value == 3: self.speed = 15

        elif value == 4: self.depth = 1
        elif value == 5: self.depth = 0

        elif value == 6: self.myview = 0
        elif value == 7: self.myview = 1
        elif value == 8: self.myview = 2

        elif value == 9: self.iShade = SolarLighting.MODE_FLAT
        elif value == 10: self.iShade = SolarLighting.MODE_SMOOTH

        elif value == 11: self.iLight1 = SolarLighting.LIGHT_ON
        elif value == 12: self.iLight1 = SolarLighting.LIGHT_OFF
        elif value == 13: # 한번 선택하면 자동회전 / 한번더 선택하면 자동회전 X
            if self.rotate == 0:
                self.rotate = 1 
                glutTimerFunc(35, self.timerFunc, 1)    
            else:   
                self.rotate = 0  
        glutPostRedisplay() 

    def init_lighting(self): # 조명 초기화

        # Enable lighting
        glEnable(GL_LIGHTING)
        # global ambient
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.ambientLight) 

        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.LIGHT0_diffuse)
        glLightfv(GL_LIGHT0, GL_SPECULAR, self.LIGHT0_specular)
        glLightfv(GL_LIGHT0, GL_AMBIENT, self.LIGHT0_ambient)
        glLightfv(GL_LIGHT0, GL_POSITION, self.LIGHT0_lightPos)

        # Enable color tracking
        glEnable(GL_COLOR_MATERIAL)

        # Set Material properties to follow glColor values
        glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.specular_ref)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.diffuse_ref)
        glMaterialfv(GL_FRONT, GL_AMBIENT, self.ambient_ref)
        glMateriali(GL_FRONT, GL_SHININESS, 128)

    def display(self):
    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Shading Control

        if (self.iShade == SolarLighting.MODE_FLAT): # 플랫일때 쉐이딩 모델 선택
            glShadeModel(GL_FLAT)
        else:
            glShadeModel(GL_SMOOTH)

        if self.depth ==1:
            glEnable(GL_DEPTH_TEST)
        else:
            glDisable(GL_DEPTH_TEST)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # front view # 지난주꺼
        if self.myview==0:	gluLookAt(0.0, 0.0, 300.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        # top view
        elif self.myview== 1: gluLookAt(0.0, 300.0, 0.0, 0.0, 0.0, 0.0,  0.0, 0.0, -1.0)
        # perspective view 
        elif self.myview== 2: gluLookAt(150.0, 150.0, 200.0, 0.0, 0.0, 0.0, -1.0, 1.0, -1.0)
        # 조명 온/오프 -> 조명을 넣었을 때 입체감이 있어야 함
        if self.iLight1 == SolarLighting.LIGHT_ON:
            glEnable(GL_LIGHT0) 
        elif self.iLight1 == SolarLighting.LIGHT_OFF:
            glDisable(GL_LIGHT0) 

        # assign light0 position to light0 here again
        glLightfv(GL_LIGHT0, GL_POSITION, self.LIGHT0_lightPos)

        glPushMatrix()
        glColor3ub(200, 200, 0)
        glutSolidSphere(15.0, 15, 15)	# Sun

        glPushMatrix()
        glRotatef(self.angle, 0.0, 1.0, 0.0)
        glTranslatef(70.0, 0.0, 0.0)
        glColor3ub(0, 255, 0)		
        glutSolidSphere(8.0, 15, 15)	# Earth
        
        glPushMatrix()
        glRotatef(self.angle, 0.0, 1.0, 0.0)
        glTranslatef(15.0, 0.0, 0.0)
        glColor3ub(255, 255, 0)
        glutSolidSphere(2.5, 15, 15)		# Moon
        glPopMatrix()
        glPopMatrix()

        # Mars
        glPushMatrix()
        glRotatef(45.0, 0.0, 0.0, 1.0)
        glRotatef(self.angle2, 0.0, 1.0, 0.0)
        glTranslatef(-100.0, 0.0, 0.0)
        glColor3ub(255, 0, 0)
        glutSolidSphere(5.0, 15, 15)				

        glPushMatrix()
        glRotatef(self.angle2, 0.0, 1.0, 0.0)
        glTranslatef(15.0, 0.0, 0.0)
        glColor3ub(0, 0, 255)
        glutSolidSphere(2.0, 15, 15)			# Mars' Moon
        glPopMatrix()
        glPopMatrix()
        glPopMatrix()

        glutSwapBuffers()
    

    def timerFunc(self, value):
    
        self.angle += 2.5
        if self.angle >= 360.0: self.angle = 0.0

        self.angle2 -= 1.2
        if self.angle2 <= 0.0: self.angle2 = 360.0

        glutPostRedisplay()

        # if rotate auto is on, call another timer function
        if self.rotate == 1:
            glutTimerFunc(self.speed, self.timerFunc, 1)

    def changeSize(self, w, h):
        
        if h == 0: h = 1
        aspect = w/h
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(45.0, aspect, 1.0, 1500.0)

    # Light position control by keyboard (z, x, a, s, q, w)
    def myKeys(self, key,  X,  Y):
    
        if key == b'z':
            self.light0_x -=10          
        elif key == b'x':
            self.light0_x +=10         
        elif key == b'a':
            self.light0_y +=10
        elif key == b's':
            self.light0_y -=10
        elif key == b'q':
            self.light0_z +=10
        elif key == b'w':
            self.light0_z -=10
        
        print("key, light pos", key, self.LIGHT0_lightPos)

        # assign light position coordinate
        self.LIGHT0_lightPos = [self.light0_x + 1.0, self.light0_y, self.light0_z + 1.0, 1.0]
        glutPostRedisplay()  

    def SpecialKeys(self, key, x, y):
        if self.rotate == 0:
            if key == GLUT_KEY_LEFT:    #earth and moon
                self.angle -= 2.0
                if self.angle <= 0.0: self.angle = 360.0
            elif key == GLUT_KEY_RIGHT:            
                self.angle += 2.0
                if self.angle >= 360.0: self.angle = 0.0

        # control mar and its moon here by Key UP and Down
            elif key == GLUT_KEY_UP:
                self.angle2 -= 2.0
                if self.angle2 <= 0.0: self.angle2 = 360.0
            elif key == GLUT_KEY_DOWN:            
                self.angle2 += 2.0
                if self.angle2 >= 360.0: self.angle2 = 0.0
        glutPostRedisplay()
    
    def main(self):
        
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(800, 600)
        glutCreateWindow("OpenGL Solar System")

        self.init_lighting()

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glutReshapeFunc(self.changeSize)
        glutDisplayFunc(self.display)

        nMenu = glutCreateMenu(self.menu)
        glutAddMenuEntry("Slow", 1)
        glutAddMenuEntry("Normal", 2)
        glutAddMenuEntry("Fast", 3)

        glutAddMenuEntry("Depth Test On", 4)
        glutAddMenuEntry("Depth Test Off", 5)

        glutAddMenuEntry("Front view", 6)
        glutAddMenuEntry("Top view", 7)
        glutAddMenuEntry("Perspective view", 8)

        glutAddMenuEntry("Flat Shading", 9)
        glutAddMenuEntry("Smooth Shading", 10)

        glutAddMenuEntry("Light on", 11)
        glutAddMenuEntry("Light off", 12)

        glutAddMenuEntry("Rotate Auto", 13)
        glutAttachMenu(GLUT_RIGHT_BUTTON)
        glutSpecialFunc(self.SpecialKeys)    
        glutKeyboardFunc(self.myKeys)    
        glutMainLoop()

s = SolarLighting()
s.main()