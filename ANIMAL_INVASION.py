import arcade

MOVEMENT_SPEED = 5
JUMP_SPEED = 20
GRAVITY = 1.8
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 700
WINDOW_HALF_WIDTH = WINDOW_WIDTH / 2
TILE_WIDTH = 70
MAP_WIDTH =300 * TILE_WIDTH
MAP_HEIGHT = 10 * TILE_WIDTH

def clamp1(value, _min, _max):
    if value <= _min:
        return _min
    if value >= _max:
        return _max
    return value

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

        # GameWindow datas
        if True:
            self.map = arcade.load_tilemap(map_file="GAME/untitled.tmj")
            self.ma = arcade.Scene.from_tilemap(self.map)
            self.collected = 0
            self.b11ool = True
            self.bool = True
            self.b1ool = True
            self.boo1l = True
            self.bo1ol = True
            self.bo1o1l = True
            self.b1o1ol = True
            self.platfor = arcade.SpriteList()
            self.banyahang =  arcade.Sound("GAME/mining-with-pick-axe-in-a-group-29590.mp3")
            self.ba = self.banyahang.play(volume= 0.5, loop=True)
            self.deathsound = arcade.Sound("GAME/male-scream-in-fear-123079.mp3")
            self.sound = arcade.Sound("GAME/X5QG74J-pirate-jumping-hut-jump.mp3")
            self.sound1 = arcade.Sound("GAME/mixkit-jumping-into-water-1304.wav")
            self.sound2 = arcade.Sound("GAME/mixkit-winning-a-coin-video-game-2069.wav")
            self.soundl = arcade.Sound("GAME/mixkit-jumping-into-water-1304.wav")
            self.damagesound = arcade.Sound("GAME/young-man-being-hurt-95628.mp3")
            self.soundjuh = arcade.Sound("GAME/hungrysheep-61124.mp3")
            self.soundcow = arcade.Sound("GAME/Polish Cow.mp3")
            self.cow = self.soundcow.play(volume=0.8, loop=True)
            self.music = arcade.Sound("GAME/Fluffing a Duck - Gaming Background Music (HD).mp3")
            self.player = self.music.play(volume=0.8, loop=True)
            self.pasztor = arcade.Sprite("GAME/pasztor.png", center_y=400, center_x=1730, flipped_horizontally=True)
            self.congrat = arcade.Sprite("GAME/congrat.png", center_y=455, center_x=20440)
            self.congrat1 = arcade.Sprite("GAME/congrat.png", center_y=455, center_x=19460)
            self.firehydrant = arcade.Sprite("GAME/FireHydrant.png", center_x=1398, center_y=90)
            self.firehydrant1 = arcade.Sprite("GAME/FireHydrant.png", center_x=14138, center_y=90)
            self.futoallatok = arcade.SpriteList()
            self.healthpoint = 100
            self.death = 0

        # Pinguin datas
        if True:
            def pinguin (x, y):
                self.pinguin1 = arcade.AnimatedTimeBasedSprite(filename="GAME/pinguin-removebg-preview.png",image_x=0,
                                                               image_y=0, image_height=80,
                                                               image_width=88.75, center_x=x, center_y=y)
                for i in range(4):
                    texture1 = arcade.load_texture("GAME/pinguin-removebg-preview.png", x= i*88.75, y= 0, width=88.75,
                                                   height=80)
                    self.pinguin1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                self.futoallatok.append(self.pinguin1)

            pinguin(17185, 105)
            pinguin(18690, 105)
            pinguin(19040, 105)

        # Miner datas
        if True:
            self.miners = arcade.SpriteList()
            def miners (x, y, flipped, time, time1):
                self.miner = arcade.AnimatedTimeBasedSprite(filename="GAME/ba11.png", image_x=0, image_y=0,
                                                             image_height=80, image_width=71, center_x=x, center_y=y)
                miner = [(71, "Game/ba11.png"), (73, "Game/ba22.png"), (78, "Game/ba33.png"),
                         (76, "Game/ba44.png"), (70, "Game/ba55.png"), (70, "Game/ba55.png"), (76, "Game/ba44.png"),
                         (78, "Game/ba33.png"), (73, "Game/ba22.png"), (71, "Game/ba11.png")]
                for width, img in miner:
                    texture1 = arcade.load_texture(img, x=0, y=0, width= width, height=80, flipped_horizontally=flipped)
                    self.miner.frames.append(arcade.AnimationKeyframe(tile_id=0, duration=time, texture=texture1))
                    texture2 = arcade.load_texture(img, x=0, y=0, width=width, height=80, flipped_horizontally=flipped)
                    self.miner.frames.append(arcade.AnimationKeyframe(tile_id=0, duration=time, texture=texture2))
                    texture3 = arcade.load_texture(img, x=0, y=0, width=width, height=80, flipped_horizontally=flipped)
                    self.miner.frames.append(arcade.AnimationKeyframe(tile_id=0, duration=time, texture=texture3))
                    texture4 = arcade.load_texture(img, x=0, y=0, width=width, height=80, flipped_horizontally=flipped)
                    self.miner.frames.append(arcade.AnimationKeyframe(tile_id=0, duration=time, texture=texture4))
                    texture5 = arcade.load_texture(img, x=0, y=0, width=width, height=80, flipped_horizontally=flipped)
                    self.miner.frames.append(arcade.AnimationKeyframe(tile_id=0, duration=time, texture=texture5))
                    texture6 = arcade.load_texture(img, x=0, y=0, width=width, height=80, flipped_horizontally=flipped)
                    self.miner.frames.append(arcade.AnimationKeyframe(tile_id=0, duration=time1, texture=texture6))
                    texture7 = arcade.load_texture(img, x=0, y=0, width=width, height=80, flipped_horizontally=flipped)
                    self.miner.frames.append(arcade.AnimationKeyframe(tile_id=0, duration=time1, texture=texture7))
                    texture8 = arcade.load_texture(img, x=0, y=0, width=width, height=80, flipped_horizontally=flipped)
                    self.miner.frames.append(arcade.AnimationKeyframe(tile_id=0, duration=time1, texture=texture8))
                    texture9 = arcade.load_texture(img, x=0, y=0, width=width, height=80, flipped_horizontally=flipped)
                    self.miner.frames.append(arcade.AnimationKeyframe(tile_id=0, duration=time1, texture=texture9))
                    texture10 = arcade.load_texture(img, x=0, y=0, width=width, height=80, flipped_horizontally=flipped)
                    self.miner.frames.append(arcade.AnimationKeyframe(tile_id=0, duration=time1, texture=texture10))
                self.miners.append(self.miner)

            self.miner_datas = [(15925, 315, True, 1, 15), (16135, 105, True, 4, 20), (15505, 385, False, 3, 18), (15225, 245, False, 2, 16)]
            for a, b, c, d, e in self.miner_datas:
                miners(a, b, c, d, e)

        # Fish datas
        if True:
            self.halspeed1 = 3
            self.halspeed2 = 3

            self.futohal1 = arcade.AnimatedWalkingSprite()
            self.futohal1.stand_left_textures.append(
                arcade.load_texture("GAME/hal.png", x=0, y=0, width=31.83, height=26,
                                    flipped_horizontally=True))
            self.futohal1.stand_right_textures.append(
                arcade.load_texture("GAME/hal.png", x=0, y=0, width=31.83, height=26))
            for i in range(3):
                texture1 = arcade.load_texture("GAME/hal.png", x=i * 31.83, y=0, width=31.83, height=26,
                                               flipped_horizontally=True)
                self.futohal1.walk_left_textures.append(texture1)
            for i in range(3):
                texture1 = arcade.load_texture("GAME/hal.png", x=i * 31.83, y=0, width=31.83, height=26)
                self.futohal1.walk_right_textures.append(texture1)
            self.futohal1.center_x = 13790
            self.futohal1.center_y = 95
            self.futoallatok.append(self.futohal1)

            self.futohal2 = arcade.AnimatedWalkingSprite()
            self.futohal2.stand_left_textures.append(
                arcade.load_texture("GAME/hal.png", x=95.49, y=0, width=31.83, height=26,
                                    flipped_horizontally=True))
            self.futohal2.stand_right_textures.append(
                arcade.load_texture("GAME/hal.png", x=95.49, y=0, width=31.83, height=26))
            for i in range(3):
                texture1 = arcade.load_texture("GAME/hal.png", x=95.49 +i * 31.83, y=0, width=31.83, height=26,
                                               flipped_horizontally=True)
                self.futohal2.walk_left_textures.append(texture1)
            for i in range(3):
                texture1 = arcade.load_texture("GAME/hal.png", x=95.49+i * 31.83, y=0, width=31.83, height=26)
                self.futohal2.walk_right_textures.append(texture1)
            self.futohal2.center_x = 14490
            self.futohal2.center_y = 95
            self.futoallatok.append(self.futohal2)

        # Rino datas
        if True:
            self.orrspeed1 = 4
            self.orrspeed2 = 4

            self.futoorr1 = arcade.AnimatedWalkingSprite()
            self.futoorr1.stand_left_textures.append(
                arcade.load_texture("GAME/1rinoceros.png", x=0, y=0, width=167.16, height=100,
                                    flipped_horizontally=True))
            self.futoorr1.stand_right_textures.append(
                arcade.load_texture("GAME/1rinoceros.png", x=0, y=0, width=167.16, height=100))
            for i in range(6):
                texture1 = arcade.load_texture("GAME/1rinoceros.png", x=i * 167.16, y=0, width=167.16, height=100,
                                               flipped_horizontally=True)
                self.futoorr1.walk_left_textures.append(texture1)
            for i in range(6):
                texture1 = arcade.load_texture("GAME/2rinoceros.png", x=i * 167.16, y=0, width=167.16, height=100,
                                               flipped_horizontally=True)
                self.futoorr1.walk_left_textures.append(texture1)
            for i in range(6):
                texture1 = arcade.load_texture("GAME/1rinoceros.png", x=i * 167.16, y=0, width=167.16, height=100)
                self.futoorr1.walk_right_textures.append(texture1)
            for i in range(6):
                texture1 = arcade.load_texture("GAME/2rinoceros.png", x=i * 167.16, y=0, width=167.16, height=100)
                self.futoorr1.walk_right_textures.append(texture1)
            self.futoorr1.center_x = 10600
            self.futoorr1.center_y = 95
            self.futoallatok.append(self.futoorr1)

            self.futoorr2 = arcade.AnimatedWalkingSprite()
            self.futoorr2.stand_left_textures.append(
                arcade.load_texture("GAME/1rinoceros.png", x=0, y=0, width=167.16, height=100,
                                    flipped_horizontally=True))
            self.futoorr2.stand_right_textures.append(
                arcade.load_texture("GAME/1rinoceros.png", x=0, y=0, width=167.16, height=100))
            for i in range(6):
                texture1 = arcade.load_texture("GAME/1rinoceros.png", x=i * 167.16, y=0, width=167.16, height=100,
                                               flipped_horizontally=True)
                self.futoorr2.walk_left_textures.append(texture1)
            for i in range(6):
                texture1 = arcade.load_texture("GAME/2rinoceros.png", x=i * 167.16, y=0, width=167.16, height=100,
                                               flipped_horizontally=True)
                self.futoorr2.walk_left_textures.append(texture1)
            for i in range(6):
                texture1 = arcade.load_texture("GAME/1rinoceros.png", x=i * 167.16, y=0, width=167.16, height=100)
                self.futoorr2.walk_right_textures.append(texture1)
            for i in range(6):
                texture1 = arcade.load_texture("GAME/2rinoceros.png", x=i * 167.16, y=0, width=167.16, height=100)
                self.futoorr2.walk_right_textures.append(texture1)
            self.futoorr2.center_x = 13000
            self.futoorr2.center_y = 95
            self.futoallatok.append(self.futoorr2)

        # Parrot datas
        if True:
            self.parrotspeed1 = 4
            self.parrotspeed2 = 4

            self.futoparrot1 = arcade.AnimatedWalkingSprite()
            self.futoparrot1.stand_left_textures.append(
                arcade.load_texture("GAME/1papagaly.png", x=0, y=0, width=66, height=60,
                                    flipped_horizontally=True))
            self.futoparrot1.stand_right_textures.append(
                arcade.load_texture("GAME/1papagaly.png", x=0, y=0, width=66, height=60))
            for i in range(9):
                texture1 = arcade.load_texture("GAME/1papagaly.png", x=i * 66, y=0, width=66, height=60,
                                               flipped_horizontally=True)
                self.futoparrot1.walk_left_textures.append(texture1)
            for i in range(9):
                texture1 = arcade.load_texture("GAME/1papagaly.png", x=i * 66, y=0, width=66, height=60)
                self.futoparrot1.walk_right_textures.append(texture1)
            self.futoparrot1.center_x = 10501
            self.futoparrot1.center_y = 500
            self.futoallatok.append(self.futoparrot1)

            self.futoparrot2 = arcade.AnimatedWalkingSprite()
            self.futoparrot2.stand_left_textures.append(
                arcade.load_texture("GAME/2papagaly.png", x=0, y=0, width=594, height=60,
                                    flipped_horizontally=True))
            self.futoparrot2.stand_right_textures.append(
                arcade.load_texture("GAME/2papagaly.png", x=0, y=0, width=594, height=60))
            for i in range(9):
                texture1 = arcade.load_texture("GAME/2papagaly.png", x=i * 66, y=0, width=66, height=60,
                                               flipped_horizontally=True)
                self.futoparrot2.walk_left_textures.append(texture1)
            for i in range(9):
                texture1 = arcade.load_texture("GAME/2papagaly.png", x=i * 66, y=0, width=66, height=60)
                self.futoparrot2.walk_right_textures.append(texture1)
            self.futoparrot2.center_x = 14700
            self.futoparrot2.center_y = 500
            self.futoallatok.append(self.futoparrot2)

        # Warrior datas
        if True:
            self.kaspeed1 = 3
            self.kaspeed2 = 3

            self.futoka1 = arcade.AnimatedWalkingSprite()
            self.futoka1.stand_left_textures.append(
                arcade.load_texture("GAME/Run.png", x=0, y=0, width=1472, height=137,
                                    flipped_horizontally=True))
            self.futoka1.stand_right_textures.append(
                arcade.load_texture("GAME/Run.png", x=0, y=0, width=1472, height=137))
            for i in range(8):
                texture1 = arcade.load_texture("GAME/Run.png", x=i * 184, y=0, width=184, height=137,
                                               flipped_horizontally=True)
                self.futoka1.walk_left_textures.append(texture1)
            for i in range(8):
                texture1 = arcade.load_texture("GAME/Run.png", x=i * 184, y=0, width=184, height=137)
                self.futoka1.walk_right_textures.append(texture1)
            self.futoka1.center_x = 8755
            self.futoka1.center_y = 125
            self.futoallatok.append(self.futoka1)

            self.futoka2 = arcade.AnimatedWalkingSprite()
            self.futoka2.stand_left_textures.append(
                arcade.load_texture("GAME/Run.png", x=0, y=0, width=1472, height=137,
                                    flipped_horizontally=True))
            self.futoka2.stand_right_textures.append(
                arcade.load_texture("GAME/Run.png", x=0, y=0, width=1472, height=137))
            for i in range(8):
                texture1 = arcade.load_texture("GAME/Run.png", x=i * 184, y=0, width=184, height=137,
                                               flipped_horizontally=True)
                self.futoka2.walk_left_textures.append(texture1)
            for i in range(8):
                texture1 = arcade.load_texture("GAME/Run.png", x=i * 184, y=0, width=184, height=137)
                self.futoka2.walk_right_textures.append(texture1)
            self.futoka2.center_x = 9460
            self.futoka2.center_y = 125
            self.futoallatok.append(self.futoka2)

        # Bear datas
        if True:
            self.medvespeed1 = 3
            self.medvespeed2 = 3

            self.futomedve1 = arcade.AnimatedWalkingSprite()
            self.futomedve1.stand_left_textures.append(
                arcade.load_texture("GAME/medve.png", x=0, y=0, width=745, height=80,
                                    flipped_horizontally=True))
            self.futomedve1.stand_right_textures.append(
                arcade.load_texture("GAME/medve.png", x=0, y=0, width=745, height=80))
            for i in range(6):
                texture1 = arcade.load_texture("GAME/medve.png", x=i * 124.16, y=0, width=124.16, height=80,
                                               flipped_horizontally=True)
                self.futomedve1.walk_left_textures.append(texture1)
            for i in range(6):
                texture1 = arcade.load_texture("GAME/medve.png", x=i * 124.16, y=0, width=124.16, height=80, )
                self.futomedve1.walk_right_textures.append(texture1)
            self.futomedve1.center_x = 6740
            self.futomedve1.center_y = 105
            self.futoallatok.append(self.futomedve1)

            self.futomedve2 = arcade.AnimatedWalkingSprite()
            self.futomedve2.stand_left_textures.append(
                arcade.load_texture("GAME/medve.png", x=0, y=0, width=745, height=80,
                                    flipped_horizontally=True))
            self.futomedve2.stand_right_textures.append(
                arcade.load_texture("GAME/medve.png", x=0, y=0, width=745, height=80))
            for i in range(6):
                texture1 = arcade.load_texture("GAME/medve.png", x=i * 124.16, y=0, width=124.16, height=80,
                                               flipped_horizontally=True)
                self.futomedve2.walk_left_textures.append(texture1)
            for i in range(6):
                texture1 = arcade.load_texture("GAME/medve.png", x=i * 124.16, y=0, width=124.16, height=80, )
                self.futomedve2.walk_right_textures.append(texture1)
            self.futomedve2.center_x = 8110
            self.futomedve2.center_y = 105
            self.futoallatok.append(self.futomedve2)

        # Eagle datas
        if True:
            self.sasspeed1 = 4
            self.sasspeed2 = 4
            self.sasspeed3 = 4
            self.sasspeed4 = 4

            self.futosas1 = arcade.AnimatedWalkingSprite()
            self.futosas1.stand_left_textures.append(
                arcade.load_texture("GAME/sas1.png", x=0, y=0, width=62.125, height=50,
                                    flipped_horizontally=True))
            self.futosas1.stand_right_textures.append(
                arcade.load_texture("GAME/sas1.png", x=0, y=0, width=62.125, height=50))
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas1.png", x=i * 62.125, y=0, width=62.125, height=50,
                                               flipped_horizontally=True)
                self.futosas1.walk_left_textures.append(texture1)
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas2.png", x=i * 62.125, y=0, width=62.125, height=50,
                                               flipped_horizontally=True)
                self.futosas1.walk_left_textures.append(texture1)
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas1.png", x=i * 62.125, y=0, width=62.125, height=50, )
                self.futosas1.walk_right_textures.append(texture1)
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas2.png", x=i * 62.125, y=0, width=62.125, height=50, )
                self.futosas1.walk_right_textures.append(texture1)
            self.futosas1.center_x = 700
            self.futosas1.center_y = 480
            self.futoallatok.append(self.futosas1)

            self.futosas2 = arcade.AnimatedWalkingSprite()
            self.futosas2.stand_left_textures.append(
                arcade.load_texture("GAME/sas1.png", x=0, y=0, width=62.125, height=50,
                                    flipped_horizontally=True))
            self.futosas2.stand_right_textures.append(
                arcade.load_texture("GAME/sas1.png", x=0, y=0, width=62.125, height=50))
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas1.png", x=i * 62.125, y=0, width=62.125, height=50,
                                               flipped_horizontally=True)
                self.futosas2.walk_left_textures.append(texture1)
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas2.png", x=i * 62.125, y=0, width=62.125, height=50,
                                               flipped_horizontally=True)
                self.futosas2.walk_left_textures.append(texture1)
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas1.png", x=i * 62.125, y=0, width=62.125, height=50, )
                self.futosas2.walk_right_textures.append(texture1)
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas2.png", x=i * 62.125, y=0, width=62.125, height=50, )
                self.futosas2.walk_right_textures.append(texture1)
            self.futosas2.center_x = 6020
            self.futosas2.center_y = 480
            self.futoallatok.append(self.futosas2)

            self.futosas3 = arcade.AnimatedWalkingSprite()
            self.futosas3.stand_left_textures.append(
                arcade.load_texture("GAME/sas1.png", x=0, y=0, width=62.125, height=50,
                                    flipped_horizontally=True))
            self.futosas3.stand_right_textures.append(
                arcade.load_texture("GAME/sas1.png", x=0, y=0, width=62.125, height=50))
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas1.png", x=i * 62.125, y=0, width=62.125, height=50,
                                               flipped_horizontally=True)
                self.futosas3.walk_left_textures.append(texture1)
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas2.png", x=i * 62.125, y=0, width=62.125, height=50,
                                               flipped_horizontally=True)
                self.futosas3.walk_left_textures.append(texture1)
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas1.png", x=i * 62.125, y=0, width=62.125, height=50, )
                self.futosas3.walk_right_textures.append(texture1)
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas2.png", x=i * 62.125, y=0, width=62.125, height=50, )
                self.futosas3.walk_right_textures.append(texture1)
            self.futosas3.center_x = 2380
            self.futosas3.center_y = 480
            self.futoallatok.append(self.futosas3)

            self.futosas4 = arcade.AnimatedWalkingSprite()
            self.futosas4.stand_left_textures.append(
                arcade.load_texture("GAME/sas1.png", x=0, y=0, width=62.125, height=50,
                                    flipped_horizontally=True))
            self.futosas4.stand_right_textures.append(
                arcade.load_texture("GAME/sas1.png", x=0, y=0, width=62.125, height=50))
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas1.png", x=i * 62.125, y=0, width=62.125, height=50,
                                               flipped_horizontally=True)
                self.futosas4.walk_left_textures.append(texture1)
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas2.png", x=i * 62.125, y=0, width=62.125, height=50,
                                               flipped_horizontally=True)
                self.futosas4.walk_left_textures.append(texture1)
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas1.png", x=i * 62.125, y=0, width=62.125, height=50, )
                self.futosas4.walk_right_textures.append(texture1)
            for i in range(8):
                texture1 = arcade.load_texture("GAME/sas2.png", x=i * 62.125, y=0, width=62.125, height=50, )
                self.futosas4.walk_right_textures.append(texture1)
            self.futosas4.center_x = 3990
            self.futosas4.center_y = 560
            self.futoallatok.append(self.futosas4)

        # Pig datas
        if True:
            self.pigspeed1 = 2
            self.pigspeed2 = 2

            self.futopig1 = arcade.AnimatedWalkingSprite()
            self.futopig1.stand_left_textures.append(
                arcade.load_texture("GAME/pig.png", x=102.666, y=0, width=102.666, height=50,
                                    flipped_horizontally=True))
            self.futopig1.stand_right_textures.append(
                arcade.load_texture("GAME/pig.png", x=102.666, y=0, width=102.666, height=50))
            for i in range(3):
                texture1 = arcade.load_texture("GAME/pig.png", x=i * 102.666, y=0, width=102.666, height=50,
                                               flipped_horizontally=True)
                self.futopig1.walk_left_textures.append(texture1)
            for i in range(3):
                texture1 = arcade.load_texture("GAME/pig.png", x=i * 102.666, y=0, width=102.666, height=50, )
                self.futopig1.walk_right_textures.append(texture1)
            self.futopig1.center_x = 2200
            self.futopig1.center_y = 95
            self.futoallatok.append(self.futopig1)

            self.futopig2 = arcade.AnimatedWalkingSprite()
            self.futopig2.stand_left_textures.append(
                arcade.load_texture("GAME/pig.png", x=102.666, y=0, width=102.666, height=50,
                                    flipped_horizontally=True))
            self.futopig2.stand_right_textures.append(
                arcade.load_texture("GAME/pig.png", x=102.666, y=0, width=102.666, height=50))
            for i in range(3):
                texture1 = arcade.load_texture("GAME/pig.png", x=i * 102.666, y=0, width=102.666, height=50,
                                               flipped_horizontally=True)
                self.futopig2.walk_left_textures.append(texture1)
            for i in range(3):
                texture1 = arcade.load_texture("GAME/pig.png", x=i * 102.666, y=0, width=102.666, height=50, )
                self.futopig2.walk_right_textures.append(texture1)
            self.futopig2.center_x = 2800
            self.futopig2.center_y = 95
            self.futoallatok.append(self.futopig2)

        # Dancing polish cow datas :)
        if True:
            self.cows = arcade.SpriteList()

            def cow (x, y):
                self.cow1 = arcade.AnimatedTimeBasedSprite(filename="GAME/T1-removebg-preview.png", image_x=0, image_y=0,
                                                           image_height=140,
                                                           image_width=303, center_x=x, center_y=y)
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/T1-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/T2-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/T3-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/t4-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/T5-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/t6-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/t7-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/t8-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/t9-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/t10-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/t11-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/t12-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/t13-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/t14-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/t15-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/t16-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/t17-removebg-preview.png", x=0, y=0, width=303, height=140)
                    self.cow1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=100, texture=texture1))
                self.cows.append(sprite=self.cow1)

            self.cow_datas = [(20090, 110), (20190, 110), (20290, 110), (20390, 110), (20490, 110),
                               (20590, 110), (20690, 110), (20790, 110), (20890, 110)]
            for x, y in self.cow_datas:
                cow(x, y)

        # Cat datas
        if True:
            self.macskaspeed1 = 4

            self.futomacska1 = arcade.AnimatedWalkingSprite()
            self.futomacska1.stand_left_textures.append(
                arcade.load_texture("GAME/macska1.png", x=0, y=0, width=58.33, height=40,
                                    flipped_horizontally=True))
            self.futomacska1.stand_right_textures.append(
                arcade.load_texture("GAME/macska1.png", x=0, y=0, width=58.33, height=40))
            for i in range(3):
                texture1 = arcade.load_texture("GAME/macska1.png", x=i * 58.33, y=0, width=58.33, height=40,
                                               flipped_horizontally=True)
                self.futomacska1.walk_left_textures.append(texture1)
            for i in range(3):
                texture2 = arcade.load_texture("GAME/macska2.png", x=i * 58.33, y=0, width=58.33, height=40,
                                               flipped_horizontally=True)
                self.futomacska1.walk_left_textures.append(texture2)
            for i in range(3):
                texture1 = arcade.load_texture("GAME/macska1.png", x=i * 58.33, y=0, width=58.33, height=40, )
                self.futomacska1.walk_right_textures.append(texture1)
            for i in range(3):
                texture2 = arcade.load_texture("GAME/macska2.png", x=i * 58.33, y=0, width=58.33, height=40, )
                self.futomacska1.walk_right_textures.append(texture2)
            self.futomacska1.center_x = 4000
            self.futomacska1.center_y = 95
            self.futoallatok.append(self.futomacska1)

        # Sheep datas
        if True:
            # Stand sheeps
            if True:
                self.juhok = arcade.SpriteList()
                self.juh1 = arcade.AnimatedTimeBasedSprite(filename="GAME/sheeps.png", image_x=0, image_y=0,
                                                               image_height=52,
                                                               image_width=511, center_x=175, center_y=305)
                for i in range(4):
                    texture1 = arcade.load_texture("GAME/sheeps.png", x=i * 127.75, y=0, width=127.75, height=52)
                    self.juh1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture1))
                for i in range(10):
                    for i in range(1):
                        texture4 = arcade.load_texture("GAME/sheeps.png", x=3*127.75, y=0, width=127.75, height=52)
                        self.juh1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture4))
                for i in range(4):
                    texture2 = arcade.load_texture("GAME/sheeps.png", x=511 -i * 127.75 - 127.75, y=0, width=127.75, height=52)
                    self.juh1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture2))
                for i in range(70):
                    for i in range(1):
                        texture3 = arcade.load_texture("GAME/sheeps.png", x=0, y=0, width=127.75, height=52)
                        self.juh1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture3))
                self.juhok.append(sprite=self.juh1)

                self.juh3 = arcade.AnimatedTimeBasedSprite(filename="GAME/sheeps.png", image_x=0, image_y=0,
                                                           image_height=52,
                                                           image_width=511, center_x=560, center_y=445)
                for i in range(10):
                    for i in range(1):
                        texture4 = arcade.load_texture("GAME/sheeps.png", x=3 * 127.75, y=0, width=127.75, height=52,
                                                       flipped_horizontally=True)
                        self.juh3.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=80, texture=texture4))
                for i in range(4):
                    texture2 = arcade.load_texture("GAME/sheeps.png", x=511 - i * 127.75 - 127.75, y=0, width=127.75,
                                                   height=52, flipped_horizontally=True)
                    self.juh3.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture2))
                for i in range(70):
                    for i in range(1):
                        texture3 = arcade.load_texture("GAME/sheeps.png", x=0, y=0, width=127.75, height=52,
                                                       flipped_horizontally=True)
                        self.juh3.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture3))
                for i in range(4):
                    texture1 = arcade.load_texture("GAME/sheeps.png", x=i * 127.75, y=0, width=127.75, height=52,
                                                   flipped_horizontally=True)
                    self.juh3.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture1))
                self.juhok.append(sprite=self.juh3)

                self.juh4 = arcade.AnimatedTimeBasedSprite(filename="GAME/sheeps.png", image_x=0, image_y=0,
                                                           image_height=52,
                                                           image_width=511, center_x=1100, center_y=95)
                for i in range(4):
                    texture2 = arcade.load_texture("GAME/sheeps.png", x=511 - i * 127.75 - 127.75, y=0, width=127.75,
                                                   height=52)
                    self.juh4.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture2))
                for i in range(70):
                    for i in range(1):
                        texture3 = arcade.load_texture("GAME/sheeps.png", x=0, y=0, width=127.75, height=52)
                        self.juh4.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture3))
                for i in range(4):
                    texture1 = arcade.load_texture("GAME/sheeps.png", x=i * 127.75, y=0, width=127.75, height=52)
                    self.juh4.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture1))
                for i in range(10):
                    for i in range(1):
                        texture4 = arcade.load_texture("GAME/sheeps.png", x=3 * 127.75, y=0, width=127.75, height=52)
                        self.juh4.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture4))
                self.juhok.append(sprite=self.juh4)
            # Running sheeps
            if True:
                self.juhspeed1 = 4
                self.juhspeed2 = 4

                self.futojuh1 = arcade.AnimatedWalkingSprite()
                self.futojuh1.stand_left_textures.append(
                    arcade.load_texture("GAME/juhfutas1.png", x=0, y=0, width=86.1666, height=52,
                                        flipped_horizontally=True))
                self.futojuh1.stand_right_textures.append(
                    arcade.load_texture("GAME/juhfutas1.png", x=0, y=0, width=86.1666, height=52))
                for i in range(6):
                    texture1 = arcade.load_texture("GAME/juhfutas1.png", x=i * 86.1666, y=0, width=86.1666, height=52,
                                                  flipped_horizontally=True)
                    self.futojuh1.walk_left_textures.append(texture1)
                for i in range(6):
                    texture2 = arcade.load_texture("GAME/juhfutas2.png", x=i * 86.1666, y=0, width=86.1666, height=52,
                                                   flipped_horizontally=True)
                    self.futojuh1.walk_left_textures.append(texture2)
                for i in range(6):
                    texture1 = arcade.load_texture("GAME/juhfutas1.png", x=i * 86.1666, y=0, width=86.1666, height=52,)
                    self.futojuh1.walk_right_textures.append(texture1)
                for i in range(6):
                    texture2 = arcade.load_texture("GAME/juhfutas2.png", x=i * 86.1666, y=0, width=86.1666, height=52,)
                    self.futojuh1.walk_right_textures.append(texture2)
                self.futojuh1.center_x = 175
                self.futojuh1.center_y = 95
                self.futoallatok.append(self.futojuh1)

                self.futojuh2 = arcade.AnimatedWalkingSprite()
                self.futojuh2.stand_left_textures.append(
                    arcade.load_texture("GAME/juhfutas1.png", x=0, y=0, width=86.1666, height=52,
                                        flipped_horizontally=True))
                self.futojuh2.stand_right_textures.append(
                    arcade.load_texture("GAME/juhfutas1.png", x=0, y=0, width=86.1666, height=52))
                for i in range(6):
                    texture1 = arcade.load_texture("GAME/juhfutas1.png", x=i * 86.1666, y=0, width=86.1666, height=52,
                                                   flipped_horizontally=True)
                    self.futojuh2.walk_left_textures.append(texture1)
                for i in range(6):
                    texture2 = arcade.load_texture("GAME/juhfutas2.png", x=i * 86.1666, y=0, width=86.1666, height=52,
                                                   flipped_horizontally=True)
                    self.futojuh2.walk_left_textures.append(texture2)
                for i in range(6):
                    texture1 = arcade.load_texture("GAME/juhfutas1.png", x=i * 86.1666, y=0, width=86.1666, height=52, )
                    self.futojuh2.walk_right_textures.append(texture1)
                for i in range(6):
                    texture2 = arcade.load_texture("GAME/juhfutas2.png", x=i * 86.1666, y=0, width=86.1666, height=52, )
                    self.futojuh2.walk_right_textures.append(texture2)
                self.futojuh2.center_x = 1300
                self.futojuh2.center_y = 95
                self.futoallatok.append(self.futojuh2)

        # Geysir datas
        if True:
            self.geysir = arcade.SpriteList()
            def geysir (x, y):
                self.geysir1 = arcade.AnimatedTimeBasedSprite(filename="GAME/1.png",image_x=0, image_y=0, image_height=456,
                                                            image_width=210, center_x= x, center_y=y)
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/1.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture1))
                for i in range(1):
                    texture2 = arcade.load_texture("GAME/2.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture2))
                for i in range(1):
                    texture3 = arcade.load_texture("GAME/3.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture3))
                for i in range(1):
                    texture4 = arcade.load_texture("GAME/4.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture4))
                for i in range(1):
                    texture5 = arcade.load_texture("GAME/5.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture5))
                for i in range(1):
                    texture6 = arcade.load_texture("GAME/6.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture6))
                for i in range(1):
                    texture7 = arcade.load_texture("GAME/7.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture7))
                for i in range(1):
                    texture8 = arcade.load_texture("GAME/8.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture8))
                for i in range(1):
                    texture9 = arcade.load_texture("GAME/9.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture9))
                for i in range(1):
                    texture9 = arcade.load_texture("GAME/9.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture9))
                for i in range(1):
                    texture8 = arcade.load_texture("GAME/8.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture8))
                for i in range(1):
                    texture7 = arcade.load_texture("GAME/7.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture7))
                for i in range(1):
                    texture6 = arcade.load_texture("GAME/6.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture6))
                for i in range(1):
                    texture5 = arcade.load_texture("GAME/5.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture5))
                for i in range(1):
                    texture4 = arcade.load_texture("GAME/4.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture4))
                for i in range(1):
                    texture3 = arcade.load_texture("GAME/3.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture3))
                for i in range(1):
                    texture2 = arcade.load_texture("GAME/2.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture2))
                for i in range(1):
                    texture1 = arcade.load_texture("GAME/1.png", x= 0, y= 0, width=210, height=456)
                    self.geysir1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture1))
                self.geysir.append(self.geysir1)
            geysir(x=1400, y=207)
            geysir(x=14140, y=247)

        # Lift datas
        if True:
            self.lift = arcade.SpriteList()
            self.liftspeed1 = 2
            self.liftspeed2 = 2
            self.liftspeed3 = 2
            self.liftspeed4 = 2
            self.liftspeed5 = 2

            self.lift1 = arcade.Sprite("GAME/lekerekitett ko1.png", image_x=0, image_y=0, image_width=70, image_height=70,
                                      center_x=17395, center_y=105)
            self.lift2 = arcade.Sprite("GAME/lekerekitett ko2.png", image_x=0, image_y=0, image_width=70, image_height=70,
                                       center_x=17535, center_y=105)
            self.lift3 = arcade.Sprite("GAME/aszfalt.png", image_x=0, image_y=0, image_width=70, image_height=70,
                                       center_x=17465, center_y=105)
            self.lift4 = arcade.Sprite("GAME/lekerekitett ko1.png", image_x=0, image_y=0, image_width=70,
                                       image_height=70,
                                       center_x=17955, center_y=460)
            self.lift5 = arcade.Sprite("GAME/lekerekitett ko2.png", image_x=0, image_y=0, image_width=70,
                                       image_height=70,
                                       center_x=18025, center_y=460)
            self.lif = [self.lift1, self.lift2, self.lift3, self.lift4, self.lift5]
            for i in self.lif:
                self.lift.append(i)

        # Bitcoin datas
        if True:
            self.bitcoins = arcade.SpriteList()

            def bitcoin (x, y):
                self.bitcoin1 = arcade.AnimatedTimeBasedSprite(filename="GAME/bitcoin2.png", image_x=0, image_y=0,
                                                               image_height=50,
                                                               image_width=27.83, center_x=x, center_y=y)
                for i in range(12):
                    texture1 = arcade.load_texture("GAME/bitcoin2.png", x=i * 27.83, y=-1, width=27.83, height=50)
                    self.bitcoin1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture1))
                for i in range(12):
                    texture2 = arcade.load_texture("GAME/bitcoin2.png", x=i * 27.83, y=49, width=27.83, height=50,
                                                   flipped_horizontally=True)
                    self.bitcoin1.frames.append(arcade.AnimationKeyframe(tile_id=i, duration=40, texture=texture2))
                self.bitcoins.append(sprite=self.bitcoin1)

            self.datas = [(175, 580), (3150, 440), (1650, 376), (4095, 95), (5150, 95), (6420, 585), (7940, 372), (8785, 95), (12145, 448), (14140, 445),
                     (17745, 515), (18760, 365), (20580, 375), (20650, 375), (15820, 375), (20720, 375), (20510, 375), (20440, 375), (20170, 375), (20090, 375)]

            for x, y in self.datas:
                bitcoin(x, y)

        # My caracter datas
        if True:
            self.katona = arcade.AnimatedWalkingSprite()
            self.katona.stand_left_textures.append(
                arcade.load_texture("GAME/Walk1.png", x=8*63.44, y=0, width=63.44, height=80))
            self.katona.stand_right_textures.append(
                arcade.load_texture("GAME/Walk1.png", x=8*63.44, y=0, width=63.44, height=80, flipped_horizontally=True))
            for i in range(9):
                texture = arcade.load_texture("GAME/Walk1.png", x=i * 63.44, y=0, width=63.44, height=80)
                self.katona.walk_left_textures.append(texture)
            for i in range(9):
                texture = arcade.load_texture("GAME/Walk1.png", x=i * 63.44, y=80, width=63.44, height=80)
                self.katona.walk_left_textures.append(texture)
            for i in range(9):
                texture = arcade.load_texture("GAME/Walk1.png", x=i * 63.44, y=0, width=63.44, height=80,
                                              flipped_horizontally=True)
                self.katona.walk_right_textures.append(texture)
            for i in range(9):
                texture = arcade.load_texture("GAME/Walk1.png", x=i * 63.44, y=80, width=63.44, height=80,
                                              flipped_horizontally=True)
                self.katona.walk_right_textures.append(texture)
            self.katona.center_x = 100
            self.katona.center_y = 170

        self.platfor.extend(self.ma["talaj"])
        self.platfor.extend(self.lift)
        self.physics = arcade.PhysicsEnginePlatformer(
            player_sprite = self.katona,
            platforms = self.platfor,
            gravity_constant = GRAVITY
        )

    def on_draw(self):
        arcade.start_render()

        drawing = [self.ma, self.geysir, self.congrat, self.congrat1, self.lift, self.miners, self.bitcoins, self.juhok, 
                   self.futoallatok, self.cows, self.pasztor, self.katona, self.firehydrant, self.firehydrant1]
        for i in drawing: 
            i.draw()

        arcade.draw_text(f"         x {self.collected}", arcade.get_viewport()[0], 650, arcade.color.GOLD,
                         font_size=20)
        arcade.draw_text("  ₿", arcade.get_viewport()[0], 640, arcade.color.GOLD,
                         font_size=40)
        arcade.draw_text(f"   HP: {self.healthpoint}", 550 + arcade.get_viewport()[0], 650, arcade.color.RED,
                         font_size=20)
        arcade.draw_text(f"    Death: {self.death}", 1100 + arcade.get_viewport()[0], 650, arcade.color.BLACK,
                         font_size=20)

    def on_update(self, delta_time: float):
        updte = [self.physics, self.futoallatok, self.katona]
        for i in updte:
            i.update()

        upanim = [self.bitcoins, self.geysir, self.miners, self.juhok, self.futoallatok, self.cows, self.katona]
        for i in upanim:
            i.update_animation()

        #Death
        if True:
            def deat():
                if self.healthpoint < 0.000001:
                    self.deathsound.play(volume=1)
                    self.death += 1
                    self.katona.center_x = 100
                    self.katona.center_y = 125
                    self.healthpoint = 100
                    if self.katona.center_x < 700:
                        change_view2 = True
                    else:
                        change_view2 = False
                    if change_view2:  # left, right, bottom, top
                        arcade.set_viewport(0,
                                            WINDOW_WIDTH,
                                            0,
                                            WINDOW_HEIGHT)
            deat()

        # Lava
        if True:
            if arcade.check_for_collision_with_list(self.katona, self.ma["lava"]):
                self.healthpoint = 0

        # Damage
        if True:
            if arcade.check_for_collision_with_list(self.katona, self.futoallatok):
                if self.b1o1ol:
                    if self.healthpoint > 25:
                        self.damagesound.play(volume=3)
                    self.healthpoint -=25
                    self.b1o1ol = False
            else:
                self.b1o1ol = True
        
        # Mine sound
        if True:
            if 14770 < self.katona.center_x < 16800:
                if self.b11ool:
                    self.ba = self.banyahang.play(volume=0.5, loop=True)
                    self.b11ool = False
            else:
                self.b11ool = True
                self.banyahang.stop(self.ba)

        # Fish swim
        if True:
            if self.futohal1.center_x < 13730:
                self.halspeed1 *= -1
            if self.futohal1.center_x > 14490:
                self.halspeed1 *= -1
            self.futohal1.change_x = self.halspeed1
            if self.futohal2.center_x < 13730:
                self.halspeed2 *= -1
            if self.futohal2.center_x > 14490:
                self.halspeed2 *= -1
            self.futohal2.change_x = self.halspeed2

        # Rino run
        if True:
            if self.futoorr1.center_x < 10500:
                self.orrspeed1 *= -1
            if self.futoorr1.center_x > 10920:
                self.orrspeed1 *= -1
            self.futoorr1.change_x = self.orrspeed1

            if self.futoorr2.center_x < 12600:
                self.orrspeed2 *= -1
            if self.futoorr2.center_x > 13160:
                self.orrspeed2 *= -1
            self.futoorr2.change_x = self.orrspeed2

        # Parrot fly
        if True:
            if self.futoparrot1.center_x < 10500:
                self.parrotspeed1 *= -1
            if self.futoparrot1.center_x > 14700:
                self.parrotspeed1 *= -1
            self.futoparrot1.change_x = self.parrotspeed1
            if self.futoparrot2.center_x < 10500:
                self.parrotspeed2 *= -1
            if self.futoparrot2.center_x > 14700:
                self.parrotspeed2 *= -1
            self.futoparrot2.change_x = self.parrotspeed2

        # Warrior run
        if True:
            if self.futoka1.center_x < 8750:
                self.kaspeed1 *= -1
            if self.futoka1.center_x > 9870:
                self.kaspeed1 *= -1
            self.futoka1.change_x = self.kaspeed1

            if self.futoka2.center_x < 8750:
                self.kaspeed2 *= -1
            if self.futoka2.center_x > 9870:
                self.kaspeed2 *= -1
            self.futoka2.change_x = self.kaspeed2

        # Bear run
        if True:
            if self.futomedve1.center_x < 6720:
                self.medvespeed1 *= -1
            if self.futomedve1.center_x > 8120:
                self.medvespeed1 *= -1
            self.futomedve1.change_x = self.medvespeed1

            if self.futomedve2.center_x < 6720:
                self.medvespeed2 *= -1
            if self.futomedve2.center_x > 8120:
                self.medvespeed2 *= -1
            self.futomedve2.change_x = self.medvespeed2

        # Eagle fly
        if True:
            if self.futosas1.center_x < 700:
                self.sasspeed1 *= -1
            if self.futosas1.center_x > 6020:
                self.sasspeed1 *= -1
            self.futosas1.change_x = self.sasspeed1
            if self.futosas2.center_x < 700:
                self.sasspeed2 *= -1
            if self.futosas2.center_x > 6020:
                self.sasspeed2 *= -1
            self.futosas2.change_x = self.sasspeed2
            if self.futosas3.center_x < 700:
                self.sasspeed3 *= -1
            if self.futosas3.center_x > 6020:
                self.sasspeed3 *= -1
            self.futosas3.change_x = self.sasspeed3
            if self.futosas4.center_x < 700:
                self.sasspeed4 *= -1
            if self.futosas4.center_x > 6020:
                self.sasspeed4 *= -1
            self.futosas4.change_x = self.sasspeed4

        # Pig run
        if True:
            if self.futopig1.center_x < 2170:
                self.pigspeed1 *= -1
            if self.futopig1.center_x > 2870:
                self.pigspeed1 *= -1
            self.futopig1.change_x = self.pigspeed1
            if self.futopig2.center_x < 2170:
                self.pigspeed2 *= -1
            if self.futopig2.center_x > 2870:
                self.pigspeed2 *= -1
            self.futopig2.change_x = self.pigspeed2

        # Congrat cow song
        if True:
            if self.katona.center_x > 19160:
                if self.bo1o1l is True:
                    self.cow = self.soundcow.play(volume=0.8, loop=True)
                    self.music.set_volume(volume=0, player=self.player)
                    self.bo1o1l = False
            else:
                self.bo1o1l = True
                self.music.set_volume(0.8, player=self.player)
                self.soundcow.stop(self.cow)

        # Cat run
        if True:
            if self.futomacska1.center_x < 3805:
                self.macskaspeed1 *= -1
            if self.futomacska1.center_x > 4385:
                self.macskaspeed1 *= -1
            self.futomacska1.change_x = self.macskaspeed1

        # Sheep run with sound
        if True:
            if self.katona.center_x < 1750:
                if self.bo1ol:
                    self.j = self.soundjuh.play(volume=0.5, loop=True)
                    self.bo1ol = False
            else:
                self.bo1ol = True
                self.soundjuh.stop(self.j)
            if self.futojuh1.center_x > 1300:
                self.juhspeed1 *= -1
            if self.futojuh1.center_x < 175:
                self.juhspeed1 *= -1
            self.futojuh1.change_x = self.juhspeed1
            if self.futojuh2.center_x > 1300:
                self.juhspeed2 *= -1
            if self.futojuh2.center_x < 175:
                self.juhspeed2 *= -1
            self.futojuh2.change_x = self.juhspeed2

        # Geysir...
        if True:
            if arcade.check_for_collision_with_list(self.katona, self.geysir):
                self.physics.gravity_constant = False
                self.katona.change_y += JUMP_SPEED/20
                if self.boo1l:
                    self.soundl.play(volume=0.5)
                    self.boo1l = False
            else:
                self.physics.gravity_constant = GRAVITY
                self.boo1l = True

        # Lift movement
        if True:
            if self.lift1.center_y > 460:
                self.liftspeed1 *= -1
            if self.lift1.center_y < 100:
                self.liftspeed1 *= -1
            self.lift1.center_y += self.liftspeed1

            if self.lift2.center_y > 460:
                self.liftspeed2 *= -1
            if self.lift2.center_y < 100:
                self.liftspeed2 *= -1
            self.lift2.center_y += self.liftspeed2

            if self.lift3.center_y > 460:
                self.liftspeed3 *= -1
            if self.lift3.center_y < 100:
                self.liftspeed3 *= -1
            self.lift3.center_y += self.liftspeed3

            if self.lift4.center_y > 460:
                self.liftspeed4 *= -1
            if self.lift4.center_y < 175:
                self.liftspeed4 *= -1
            self.lift4.center_y += self.liftspeed4

            if self.lift5.center_y > 460:
                self.liftspeed5 *= -1
            if self.lift5.center_y < 175:
                self.liftspeed5 *= -1
            self.lift5.center_y += self.liftspeed5

        # Main caracter view
        if True:
            if WINDOW_HALF_WIDTH < self.katona.center_x < MAP_WIDTH - WINDOW_HALF_WIDTH:
                change_view = True
            else:
                change_view = False
            if change_view:  # left, right, bottom, top
                arcade.set_viewport(self.katona.center_x - WINDOW_HALF_WIDTH,
                                    self.katona.center_x + WINDOW_HALF_WIDTH,
                                    0,
                                    WINDOW_HEIGHT)
            self.katona.center_x = clamp1(self.katona.center_x, 25, MAP_WIDTH - 25)

        # Water sound
        if True:
            if arcade.check_for_collision_with_list(self.katona, self.ma["viz"]):
                if self.bool:
                    self.sound1.play(volume=0.5)
                    self.bool = False
            else:
                self.bool= True

        # Bitcoin sound
        if True:
            collected = arcade.check_for_collision_with_list(self.katona, self.bitcoins)
            for i in collected:
                i.kill()
                self.collected +=1
                self.sound2.play(volume=0.8)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.katona.change_x = MOVEMENT_SPEED
        if symbol == arcade.key.D:
            self.katona.change_x = MOVEMENT_SPEED
        if symbol == arcade.key.LEFT:
            self.katona.change_x = -MOVEMENT_SPEED
        if symbol == arcade.key.A:
            self.katona.change_x = -MOVEMENT_SPEED
        if symbol == arcade.key.UP:
            if self.physics.can_jump():
                self.katona.change_y = JUMP_SPEED
                self.sound.play(volume=0.7)
        if symbol == arcade.key.W:
            if self.physics.can_jump():
                self.katona.change_y = JUMP_SPEED
                self.sound.play(volume=0.7)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.katona.change_x = 0
        if symbol == arcade.key.D:
            self.katona.change_x =0
        if symbol == arcade.key.LEFT:
            self.katona.change_x = 0
        if symbol == arcade.key.A:
            self.katona.change_x = 0
        if symbol == arcade.key.UP:
            if self.physics.can_jump():
                self.katona.change_y = 0
        if symbol == arcade.key.W:
            if self.physics.can_jump():
                self.katona.change_y = 0

GameWindow(WINDOW_WIDTH, WINDOW_HEIGHT, "ANIMAL INVASION")
arcade.run()
