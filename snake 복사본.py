import random
import pygame  # 파이게임 모듈 임포트하기
from datetime import datetime
from datetime import timedelta

'''
해야할
1.p를 누를시 게임정지
2.r를 누를시 게임 리스타트


'''

# 여러 가지 색
RED = 255, 0, 0  # 적색:   적 255, 녹   0, 청   0
GREEN = 0, 255, 0  # 녹색:   적   0, 녹 255, 청   0
BLUE = 0, 0, 255  # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127  # 보라색: 적 127, 녹   0, 청 127
BLACK = 0, 0, 0  # 검은색: 적   0, 녹   0, 청   0
GRAY = 127, 127, 127  # 회색:   적 127, 녹 127, 청 127
WHITE = 255, 255, 255  # 하얀색: 적 255, 녹 255, 청 255

# 블록을 그리는 함수 정의하기
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 540
BLOCK_SIZE = 20


# 뱀 게임에서 사용할 데이터 모델 정의하기


class Snake:
    """뱀 클래스"""
    color = GREEN  # 뱀의 색

    def __init__(self):
        self.positions = [(9, 6), (9, 7), (9, 8), (9, 9)]  # 뱀의 위치
        self.direction = 'north'  # 뱀의 방향

    def draw(self, vIew_screen):
        """뱀을 화면에 그린다."""
        for position in self.positions:  # 뱀의 몸 블록들을 순회하며
            draw_block(vIew_screen, self.color, position)  # 각 블록을 그린다

    def crawl(self):
        """뱀이 현재 방향으로 한 칸 기어간다."""
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'north':
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'south':
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'west':
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'east':
            self.positions = [(y, x + 1)] + self.positions[:-1]

    def turn(self, direction):
        """뱀의 방향을 바꾼다."""
        if self.direction == 'north' and direction == 'south':
            pass

        elif self.direction == 'south' and direction == 'north':
            pass

        elif self.direction == 'east' and direction == 'west':
            pass

        elif self.direction == 'west' and direction == 'east':
            pass

        else:
            self.direction = direction

    def grow(self):

        """뱀이 한 칸 자라나게 한다."""
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'north':
            self.positions.append((y - 1, x))
        elif self.direction == 'south':
            self.positions.append((y + 1, x))
        elif self.direction == 'west':
            self.positions.append((y, x - 1))
        elif self.direction == 'east':
            self.positions.append((y, x + 1))


class Wall:
    """벽 클래스"""
    color = GRAY

    def __init__(self):
        self.position = []

        for i in range(SCREEN_HEIGHT):
            self.position.append((i + 2, SCREEN_WIDTH / BLOCK_SIZE - 1))
            self.position.append((i + 2, 0))

        for k in range(SCREEN_WIDTH):
            self.position.append((SCREEN_HEIGHT / BLOCK_SIZE - 1, k))
            self.position.append((2, k))

    def draw(self, screen):
        """장애물을 화면에 그린다."""
        for position in self.position:
            draw_block(screen, self.color, position)


class Obstacle(Wall):
    """장애물 클래스"""
    obstacle_count = 0

    def added_obstacle(self):
        self.position.append((random.randint(3, 25), random.randint(1, 18)))
        self.obstacle_count += 1

    def draw(self, screen):
        for obstacle_position in self.obstacle_count:
            draw_block(screen, self.color, obstacle_position)


class Apple:
    """사과 클래스"""
    color = RED  # 사과의 색

    def __init__(self, apple_position=(random.randint(3, 25), random.randint(1, 18))):
        self.apple_position = apple_position  # 사과의 위치

    def draw(self, screen):
        """사과를 화면에 그린다."""
        draw_block(screen, self.color, self.apple_position)


class Poison_apple:
    """독사과 클래스"""
    color = PURPLE  # 독사과의 색
    poison_position = []  # 독사과의 위치
    poison_apple_count = 0

    def __init__(self, apple_count):
        self.poison_position = []
        self.poison_apple_count = apple_count

        for poison_pisiotno in range(self.poison_apple_count):
            self.poison_position.append((random.randint(3, 25), random.randint(1, 18)))

    def draw(self, screen):
        """독사과를 화면에 그린다"""
        for poison_apple_positon in self.poison_position:
            draw_block(screen, self.color, poison_apple_positon)


class GameBoard:
    """게임판 클래스"""
    width = 20  # 게임판의 너비
    height = 20  # 게임판의 높이
    apple_count = 0  # 먹은 사과의 개수

    def __init__(self):
        self.snake = Snake()  # 게임판 위의 뱀
        self.apple = Apple()  # 게임판 위의 사과
        self.wall = Wall()  # 게임판 위의 장애물
        self.poison_apple = Poison_apple(self.apple_count)  # 게임판 위의 독사과
        self.obstacle = Obstacle()  # 게임판 위의 장애물

    def draw(self, screen):
        """화면에 게임판의 구성요소를 그린다."""
        self.apple.draw(screen)  # 게임판 위의 사과를 그린다
        self.snake.draw(screen)  # 게임판 위의 뱀을 그린다
        self.wall.draw(screen)  # 게임판 위의 장애물을 그린
        self.poison_apple.draw(screen)  # 게임판 위의 독사과를 그린
        self.obstacle.draw(screen)  # 게임판 위의 장애물


    def count_apple(self):

        """사과 카운트 하나증가"""
        self.apple_count += 1

    def decount_apple(self):
        """사과 카운트 하나 감소"""
        self.apple_count -= 1

    def put_new_apple(self):
        """게임판에 새 사과를 놓는다."""
        self.apple = Apple((random.randint(3, 25), random.randint(1, 18)))
        for snake_position in self.snake.positions:  # ❸ 뱀 블록을 순회하면서
            if self.apple.apple_position == snake_position:  # 사과가 뱀 위치에 놓인 경우를 확인해
                self.put_new_apple()  # 사과를 새로 놓는다
                break

    def put_new_posionapple(self):
        """게임판에 독사과를 새로 놓는다"""
        self.poison_apple = Poison_apple(self.apple_count)
        for snake_position in self.snake.positions:
            if self.poison_apple.poison_position == snake_position:
                self.put_new_posion_apple()
                break

    def process_turn(self):
        """게임을 한 차례 진행한다."""
        self.snake.crawl()

        # 뱀의 머리가 뱀의 몸과 부딛혔으면
        if self.snake.positions[0] in self.snake.positions[1:]:
            raise SnakeCollisionException()  # 뱀 충돌 예외를 일으킨다

        # 뱀의 머리가 사과를 먹으면
        if self.snake.positions[0] == self.apple.apple_position:
            self.snake.grow()  # 뱀을 자라게 한다
            self.put_new_apple()  # 새로운 사과를 나둔다
            self.count_apple()  # 카운트 하나 증가시킨다
            self.put_new_posionapple()  # 독사과를 다시 배치한

        # 뱀의 머리가 벽과 부딛혓으면
        if self.snake.positions[0] in self.wall.position:
            raise SnakeCollisionException()  # 뱀 충돌 예외를 일으킨다

        # 사과가 벽과 접촉시
        if self.apple.apple_position in self.wall.position:
            self.put_new_apple()
            self.decount_apple()

        # 뱀의 머리가 독사과를 먹을시
        if self.snake.positions[0] in self.poison_apple.poison_position:
            self.decount_apple()
            self.put_new_posionapple()

        # 사고와 독사과가 겹칠시
        if self.apple.apple_position in self.poison_apple.poison_position:
            self.put_new_apple()
            self.put_new_posionapple()

        #  사과 카운팅이 3의 배수가 될시
        if self.apple_count == 0:
            pass
        elif self.apple_count % 3 == 0:
            self.obstacle.added_obstacle()
        else:
            pass


class SnakeCollisionException(Exception):
    """뱀 충돌 예외"""
    pass


def draw_background(screen):
    """게임의 배경을 그린다."""
    background = pygame.Rect((0, 40), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)


def draw_block(screen, color, position):
    """position 위치에 color 색깔의 블록을 그린다."""
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)


def update_points(filed, point):
    font = pygame.font.Font(None, 30)
    input_box = pygame.Rect((0, 0), (SCREEN_WIDTH, 40))
    pygame.draw.rect(filed, BLACK, input_box)
    text_surface = font.render("Points: " + str(point), True, pygame.Color('lightskyblue3'))
    filed.blit(text_surface, (input_box.x + 10, input_box.y + 10))


pygame.init()

# 지정한 크기의 게임 화면 창을 연다.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

block_position = [0, 0]  # 블록의 위치 (y, x)
last_moved_time = datetime.now()  # 마지막으로 블록을 움직인 때

# 종료 이벤트가 발생할 때까지 게임을 계속 진행한다
# 방향키 입력에 따라 바꿀 블록의 방향
DIRECTION_ON_KEY = {
    pygame.K_UP: 'north',
    pygame.K_DOWN: 'south',
    pygame.K_LEFT: 'west',
    pygame.K_RIGHT: 'east',
}
block_direction = 'east'  # 블록의 방향
block_position = [0, 0]
last_turn_time = datetime.now()

game_board = GameBoard()  # 게임판 인스턴스를 생성한다

TURN_INTERVAL = timedelta(seconds=0.1)  # 게임 진행 간격을 0.1초로 정의한다

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:  # 화살표 키가 입력되면 뱀의 방향을 바꾼다
            if event.key in DIRECTION_ON_KEY:
                game_board.snake.turn(DIRECTION_ON_KEY[event.key])

    # 시간이 TURN_INTERVAL만큼 지날 때마다 게임을 한 차례씩 진행한다
    if TURN_INTERVAL < datetime.now() - last_turn_time:
        try:
            update_points(screen, game_board.apple_count)
            game_board.process_turn()
        except SnakeCollisionException:
            exit()
        last_turn_time = datetime.now()

    draw_background(screen)
    game_board.draw(screen)
    pygame.display.update()
