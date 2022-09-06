import pygame,sys

pygame.init()

#프로그램 제목 설정
pygame.display.set_caption("비주얼 노벨 GUI 테스트1")

#변수
WHITE = (255,255,255)
BLACK = (0,0,0)
Screen_size=[1280,720]

#기본값
screen = pygame.display.set_mode(Screen_size)
font = pygame.font.SysFont("Verdana",20)
done = False


#해상도 바꾸기 함수
def resChange(Swidth,Sheight):
    Screen_size[0]=Swidth
    Screen_size[1]=Sheight
    screen = pygame.display.set_mode(Screen_size)
    

#문자 출력 함수
'''문자 출력 자체는 됩니다만, 해상도를 변경했을 때 같이 크기가 변경되지 않아서
방법을 찾고 있습니다. 다음에 올라오는 버전은 이를 수정한 방법일 겁니다.'''
def Talk(Message,txtColor='BLACK',start_pos=(50,50)):
    textSurface = font.render(Message,True,pygame.Color(txtColor),None)
    textRect = textSurface.get_rect()
    textRect.midbottom = start_pos

    screen.blit(textSurface,textRect)



#메인 루프    
while not done:
    
    screen.fill(WHITE)
 
    for event in pygame.event.get():
        
        #해상도 변경(키보드 1,2,3 입력)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                resChange(1280,720)
            elif event.key == pygame.K_2:
                resChange(1600,900)
            elif event.key == pygame.K_3:
                resChange(1920,1080)
            
        #윈도우 창의 x를 눌렀을 때 종료
        elif event.type == pygame.QUIT:
            done = True


        
        pygame.display.flip()

pygame.quit()