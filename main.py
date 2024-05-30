import sys
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Dimensiones de la ventana
window_width = 800
window_height = 600

# Número de filas del Triángulo de Pascal
num_rows = 10

def pascal_triangle(n):
    """Genera el Triángulo de Pascal hasta la fila n."""
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)
    return triangle

def draw_triangle(triangle):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluOrtho2D(0, window_width, 0, window_height)
    
    base_x = window_width // 2
    base_y = window_height - 50
    dy = 30
    dx = 15
    
    for i, row in enumerate(triangle):
        x = base_x - (dx * i)
        y = base_y - (dy * i)
        for num in row:
            draw_text(str(num), x, y)
            x += 2 * dx

    glutSwapBuffers()

def draw_text(text, x, y):
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    global window_width, window_height, num_rows
    
    # Inicializar GLUT
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(window_width, window_height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"prueba")
    
    # Inicializar OpenGL
    glClearColor(0.1, 0.1, 0.1, 1.0)
    
    # Generar el Triángulo de Pascal
    triangle = pascal_triangle(num_rows)
    
    # Funciones de callback
    glutDisplayFunc(lambda: draw_triangle(triangle))
    glutReshapeFunc(resize)
    
    # Iniciar el loop de GLUT
    glutMainLoop()

if __name__ == "__main__":
    main()
