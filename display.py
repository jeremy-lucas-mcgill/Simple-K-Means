import pygame
import matplotlib.pyplot as plt
from data import Data
from kmeans import KMeans
from config import *

data = Data(x_min=0,x_max=50,y_min=0,y_max=100,clusters=5,points_per_cluster=[50,100],scale=2,offset=[5,30])
clf = KMeans(num_clusters=5)
start_clusters, start_cluster_list = clf.initalize(data)


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
scaleX = (WIDTH - 2*BORDER)/(data.x_max - data.x_min)
scaleY = (HEIGHT - 2*BORDER)/(data.y_max - data.y_min)
offsetX = BORDER
offsetY = HEIGHT - BORDER

def draw_graph(clusters,cluster_list):
    pygame.draw.line(screen,BLACK, (BORDER,HEIGHT-BORDER),(WIDTH-BORDER,HEIGHT-BORDER))
    pygame.draw.line(screen,BLACK, (BORDER,BORDER),(BORDER,HEIGHT-BORDER))
    for index in range(len(cluster_list)):
        for (x,y) in cluster_list[index]:
            screen_x = scaleX * x + offsetX
            screen_y = -scaleY * y + offsetY
            pygame.draw.circle(screen, COLORS[index],(screen_x,screen_y),5)
    for (x,y) in clusters:
        screen_x = scaleX * x + offsetX
        screen_y = -scaleY * y + offsetY
        pygame.draw.circle(screen, BLACK,(screen_x,screen_y),10)

draw_graph(start_clusters,start_cluster_list)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    #draw graph
    clusters,cluster_list = clf.single_iteration_fit(data)
    draw_graph(clusters,cluster_list)
    pygame.display.flip()
    clock.tick(60)
    pygame.time.wait(1000)
pygame.quit()