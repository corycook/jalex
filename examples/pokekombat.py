# PokeKombat!!!
# The mystical Pokemon Eevee must fight his way through countless enemies to prove his worth
# Hyper beam is now swift, I feel Eevee would die if he actually used-
# Hyper beam as much as he was origanally expected to.

# Add costom poke death animation so a new pokeball comes up

# Make Eevee and Psyduck not collideable just like scyther and just make
# missiles collideable

from v1shim import games, color
import math, random

Missile_Odds = 1


games.init(screen_width=840, screen_height=480, fps=50)


class Psyduck(games.Sprite):
    """
    An evil Psyduck!!!
    """
    image = games.load_image("psyduck.png")
    sound = games.load_sound("cubone.wav")
    MISSILE_DELAY = 25
    Left = False
    Right = False
    total = 0
    stone = 0
    odds = 2
    missile_odds = 100
    health = games.Text(value=100,
                        size=30,
                        color=color.blue,
                        top=5,
                        right=games.screen.width - 20,
                        is_collideable=False)
    games.screen.add(health)

    def __init__(self, game, x, y, speed=2, odds_change=200):
        """ Initialize Psyduck! """
        Psyduck.total += 1
        super(Psyduck, self).__init__(image=Psyduck.image,
                                      x=x, y=y, dx=speed)
        self.odds_change = odds_change
        self.missile_wait = 0

    def die(self):
        size = 9
        Psyduck.total -= 1
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        new_cubone = Cubone(x=self.x, y=self.y, size=size)
        games.screen.add(new_cubone)
        stone = random.randint(1, 3)
        if stone == 2:
            new_waterstone = Water_Stone(game=self,
                                         x=400,
                                         y=2)
            games.screen.add(new_waterstone)
            Psyduck.sound.play()
        if stone == 1:
            new_thunderstone = Thunder_Stone(game=self,
                                             x=400,
                                             y=2)
            games.screen.add(new_thunderstone)
            Psyduck.sound.play()
        if stone == 3:
            new_firestone = Fire_Stone(game=self,
                                       x=400,
                                       y=2)
            games.screen.add(new_firestone)
            Psyduck.sound.play()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def decrease_health(self):
        Psyduck.health.value -= 10
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def update(self):
        """IT'S ALIVEEEEE!!!!!"""

        if random.randrange(self.odds_change) == 0:
            self.odds += 1
            self.dx = -self.dx

        if random.randrange(self.missile_odds) == 0:

            new_bubble = Bubble(self.x, self.y)
            games.screen.add(new_bubble)
            self.bubble_wait = Psyduck.MISSILE_DELAY

        if self.odds % 2 == 0:
            image2 = games.load_image("psyduck2.bmp")
            self.set_image(image2)
            Psyduck.Left = False
            Psyduck.Right = True

        else:
            image = games.load_image("psyduck.png")
            self.set_image(image)
            Psyduck.Left = True
            Psyduck.Right = False

        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

       # if self.overlapping_sprites:
        #    PsyduckStats[0] = PsyduckStats[0] - 10

        if self.health.value <= 0:
            self.die()


class Cubone(games.Sprite):
    """
    An evil Cubone!!!
    """
    image = games.load_image("cubone.png")
    MISSILE_DELAY = 25
    Left = False
    Right = False
    total = 0
    odds = 2  # must add this
    missile_odds = 100  # must add this too
    sound = games.load_sound("charizard.wav")
    health = games.Text(value=100,
                        size=30,
                        color=color.brown,
                        top=25,
                        right=games.screen.width - 20,
                        is_collideable=False)
    games.screen.add(health)

    def __init__(self, size, x, y, speed=2, odds_change=200):
        """ Initialize Cubone! """
        Cubone.total += 1
        super(Cubone, self).__init__(image=Cubone.image,
                                     x=x, y=y, dx=speed)
        self.odds_change = odds_change
        self.missile_wait = 0

    def decrease_health(self):
        Cubone.health.value -= 10
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die(self):
        size = 9
        Cubone.total -= 1
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        new_charizard = Charizard(x=self.x, y=self.y, size=size)
        games.screen.add(new_charizard)
     #   new_firestone = Fire_Stone(game = self,
      #                                        x = 400,
       #                                       y = 2)
       # games.screen.add(new_firestone)
        Cubone.sound.play()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def update(self):
        """IT'S ALIVEEEEE!!!!!"""

        self.size = 9

        if random.randrange(self.odds_change) == 0:
            self.odds += 1  # add this
            self.dx = -self.dx

        if random.randrange(self.missile_odds) == 0:  # add this too

            new_bone = Bone(self.x, self.y)
            games.screen.add(new_bone)
            self.bubble_wait = Cubone.MISSILE_DELAY

        if self.odds % 2 == 0:  # ADD ALL OF THIS
            image2 = games.load_image("cubone2.bmp")
            self.set_image(image2)
            Cubone.Left = False
            Cubone.Right = True

        else:
            image = games.load_image("cubone.png")
            self.set_image(image)
            Cubone.Left = True
            Cubone.Right = False
            # To here ^^^^^
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

        # if self.overlapping_sprites:
         #   CuboneStats[0] = CuboneStats[0] - 10

        if self.health.value <= 0:
            self.die()


class Charizard(games.Sprite):
    """
    An evil Cubone!!!
    """
    image = games.load_image("charizard.png")
    MISSILE_DELAY = 25
    Left = False
    Right = False
    total = 0
    odds = 2
    missile_odds = 100
    sound = games.load_sound("snorlax.wav")
    health = games.Text(value=100,
                        size=30,
                        color=color.red,
                        top=45,
                        right=games.screen.width - 20,
                        is_collideable=False)
    games.screen.add(health)

    def __init__(self, size, x, y, speed=3, odds_change=100):
        """ Initialize Cubone! """
        Charizard.total += 1
        super(Charizard, self).__init__(image=Charizard.image,
                                        x=x, y=y, dx=speed)
        self.odds_change = odds_change
        self.missile_wait = 0

    def decrease_health(self):
        Charizard.health.value -= 10
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die(self):
        size = 9
        Charizard.total -= 1
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        new_snorlax = Snorlax(x=self.x, y=self.y, size=size)
        games.screen.add(new_snorlax)
   #     new_thunderstone = Thunder_Stone(game = self,
    #                                          x = 400,
     #                                         y = 2)
     #   games.screen.add(new_thunderstone)
        Charizard.sound.play()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def update(self):
        """IT'S ALIVEEEEE!!!!!"""

        self.size = 9

        if random.randrange(self.odds_change) == 0:
            self.odds += 1
            self.dx = -self.dx
        if random.randrange(self.missile_odds) == 0:

            new_Fireball = Fireball(self.x, self.y)
            games.screen.add(new_Fireball)
            self.bubble_wait = Charizard.MISSILE_DELAY

        if self.odds % 2 == 0:  # ADD ALL OF THIS
            image2 = games.load_image("charizard2.bmp")
            self.set_image(image2)
            Charizard.Left = False
            Charizard.Right = True

        else:
            image = games.load_image("charizard.png")
            self.set_image(image)
            Charizard.Left = True
            Charizard.Right = False

        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

        # if self.overlapping_sprites:
         #   CuboneStats[0] = CuboneStats[0] - 10

        if self.health.value <= 0:
            self.die()


class Snorlax(games.Sprite):
    """
    An really cute Snorlax!!!
    """
    image = games.load_image("snorlax.png")
    MISSILE_DELAY = 25
    Left = False
    Right = False
    total = 0
    odds = 2
    boundary1 = 0
    boundary2 = 0
    missile_odds = 100
    jump_odds = 100
    sound = games.load_sound("mewtwo.wav")
    sound2 = games.load_sound("snorlax2.wav")
    health = games.Text(value=100,
                        size=30,
                        color=color.white,
                        top=65,
                        right=games.screen.width - 20,
                        is_collideable=False)
    games.screen.add(health)

    def __init__(self, size, x, y, speed=3, odds_change=100):
        """ Initialize Snorlax! """
        Snorlax.total += 1
        super(Snorlax, self).__init__(image=Snorlax.image,
                                      x=x, y=y, dx=speed)
        self.odds_change = odds_change
        self.missile_wait = 0

    def decrease_health(self):
        Snorlax.health.value -= 10
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die(self):
        size = 9
        Snorlax.total -= 1
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        new_mewtwo = Mewtwo(x=self.x, y=400, size=size)
        games.screen.add(new_mewtwo)
   #     new_thunderstone = Thunder_Stone(game = self,
    #                                          x = 400,
     #                                         y = 2)
     #   games.screen.add(new_thunderstone)
        Snorlax.sound.play()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def update(self):
        """IT'S ALIVEEEEE!!!!!"""

        self.size = 9
        self.boundary1 = self.x + 350
        self.boundary2 = self.x - 350
        if random.randrange(self.odds_change) == 0:
            self.odds += 1
            self.dx = -self.dx
        if random.randrange(self.jump_odds) == 0:
            self.dy = - 5
            Snorlax.sound2.play()

        if self.bottom < 350:

            self.dy = -self.dy

        if self.top > 390:
            self.dy = 0
            self.y = 400

        if self.top > 400:
            self.dy = 0
            self.y = 400

       # if random.randrange(self.missile_odds) ==0:

        #    new_Fireball = Fireball(self.x, self.y)
         #   games.screen.add(new_Fireball)
          #  self.bubble_wait = Snorlax.MISSILE_DELAY

        if self.odds % 2 == 0:  # ADD ALL OF THIS
            image2 = games.load_image("snorlax2.bmp")
            self.set_image(image2)
            Charizard.Left = False
            Charizard.Right = True

        else:
            image = games.load_image("snorlax.png")
            self.set_image(image)
            Charizard.Left = True
            Charizard.Right = False

        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

        # if self.overlapping_sprites:
         #   CuboneStats[0] = CuboneStats[0] - 10

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.decrease_health()
                if sprite.x < self.x:
                    self.x += 50
                    sprite.x -= 50  # this will make sprite fall back when hit
                else:
                    sprite.x += 50
                    self.x -= 50

        if self.health.value <= 0:
            self.die()


class Mewtwo(games.Sprite):
    """
    An evil Mewtwo!!!
    """
    image = games.load_image("mewtwo.png")
    MISSILE_DELAY = 25
    Left = False
    Right = False
    odds = 2
    missile_odds = 50
    health = games.Text(value=150,
                        size=30,
                        color=color.purple,
                        top=85,
                        right=games.screen.width - 20,
                        is_collideable=False)
    games.screen.add(health)

    def __init__(self, size, x, y, speed=3, odds_change=100):
        """ Initialize Mewtwo! """
        super(Mewtwo, self).__init__(image=Mewtwo.image,
                                     x=x, y=y, dx=speed)
        self.odds_change = odds_change
        self.missile_wait = 0

    def win(self):
        """Ends game"""
        end_message = games.Message(value="You Win!",
                                    size=90,
                                    color=color.blue,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        games.screen.add(end_message)

    def decrease_health(self):
        Mewtwo.health.value -= 10
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        self.win()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def update(self):
        """IT'S ALIVEEEEE!!!!!"""

        self.size = 9

        if random.randrange(self.odds_change) == 0:
            self.odds += 1
            self.dx = -self.dx

        if random.randrange(self.missile_odds) == 0:

            new_Shadowball = Shadowball(self.x, self.y)
            games.screen.add(new_Shadowball)
            self.bubble_wait = Mewtwo.MISSILE_DELAY

        if self.odds % 2 == 0:  # ADD ALL OF THIS
            image2 = games.load_image("mewtwo2.png")
            self.set_image(image2)
            Mewtwo.Left = False
            Mewtwo.Right = True

        else:
            image = games.load_image("mewtwo.png")
            self.set_image(image)
            Mewtwo.Left = True
            Mewtwo.Right = False

        # if self.overlapping_sprites:
         #   CuboneStats[0] = CuboneStats[0] - 10

        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

        if self.health.value <= 0:
            self.die()


class Eevee(games.Sprite):
    """
    An Eevee that is ready to fight!
    """
    image = games.load_image("eevee.png")
    sound = games.load_sound("eevee3.wav")
    soundend = games.load_sound("gameover.wav")
    MISSILE_DELAY = 25
    JUMP_DELAY = 50
    Left = False
    Right = False
    total = 0
    health = games.Text(value=100,
                        size=30,
                        color=color.red,
                        top=5,
                        right=games.screen.width - 710,
                        is_collideable=False)
    games.screen.add(health)
    stone = games.Text(value="Eevee",
                       size=30,
                       color=color.white,
                       top=5,
                       right=games.screen.width - 745,
                       is_collideable=False)
    games.screen.add(stone)

    def __init__(self, x, y):
        """ Initialize Eevee like a boss, and keeps his score."""
        super(Eevee, self).__init__(image=Eevee.image,
                                    x=x, y=y)
        self.missile_wait = 0
        self.jump_wait = 0

    def end(self):
        """Ends game"""
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        Eevee.soundend.play()
        games.screen.add(end_message)

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        self.end()

    def die2(self):
        Eevee.total = 1
        size = 9
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        self.health.destroy()
        self.stone.destroy()
        Jolteon.health.destroy()
        Flareon.health.destroy()
        Jolteon.stone.destroy()
        Flareon.stone.destroy()
        new_vaporeon = Vaporeon(x=400, y=400)
        games.screen.add(new_vaporeon)
        # Charizard.sound.play()

    def die3(self):
        Eevee.total = 2
        size = 9
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        self.health.destroy()
        self.stone.destroy()
        Vaporeon.health.destroy()
        Flareon.health.destroy()
        Vaporeon.stone.destroy()
        Flareon.stone.destroy()
        new_jolteon = Jolteon(x=self.x, y=400)
        games.screen.add(new_jolteon)

    def die4(self):
        Eevee.total = 3
        size = 9
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        self.health.destroy()
        self.stone.destroy()
        Vaporeon.health.destroy()
        Jolteon.health.destroy()
        Vaporeon.stone.destroy()
        Jolteon.stone.destroy()
        new_flareon = Flareon(x=self.x, y=400)
        games.screen.add(new_flareon)

    def die5(self):
        Eevee.total = 4
        size = 9
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        self.health.destroy()
        self.stone.destroy()
        new_mew = Mew(x=self.x, y=400)
        games.screen.add(new_mew)

    def decrease_health(self):
        Eevee.health.value -= 10
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def water_evolve(self):
        Eevee.stone.value = "Vaporean"

    def update(self):
        """Move and jump around! Just like Eevee in real life!!!"""
        if games.keyboard.is_pressed(games.K_LEFT):
            image2 = games.load_image("eevee2.bmp")
            self.set_image(image2)
            Eevee.Left = True
            Eevee.Right = False
            self.x -= 2
        if games.keyboard.is_pressed(games.K_RIGHT):
            image = games.load_image("eevee.png")
            self.set_image(image)
            Eevee.Left = False
            Eevee.Right = True
            self.x += 2

        if games.keyboard.is_pressed(games.K_1) and games.keyboard.is_pressed(games.K_5) and games.keyboard.is_pressed(games.K_0):
            self.die5()

        if games.keyboard.is_pressed(games.K_UP) and self.jump_wait == 0:
            Eevee.sound.play()
            self.jump_wait = Eevee.JUMP_DELAY

            self.dy = -4
        if self.bottom < 350:

            self.dy = -self.dy

        if self.top > 360:
            self.dy = 0
            self.y = 400

        # HEALTH
       # if self.overlapping_sprites:
        #    EeveeStats[0] = EeveeStats[0] - 10
         #   Eevee.health.value -= 10
        if self.health.value == 0:
            self.die()

        # Wraps Eevee around screen lol
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        # If waiting until eevee can use Hyper Beam again decrease wait.
        if self.missile_wait > 0:
            self.missile_wait -= 1
        # If waiting until eevee can jum again decrease wait.
        if self.jump_wait > 0:
            self.jump_wait -= 1

        # Use Hyper Beam if spacebar pressed and missile wait is over
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y)
            games.screen.add(new_missile)
            self.missile_wait = Eevee.MISSILE_DELAY


class Vaporeon(games.Sprite):
    """
    A Vaporeon that is ready to fight!
    """
    image = games.load_image("vaporeon.png")
    sound = games.load_sound("vaporeon.wav")
    soundend = games.load_sound("gameover.wav")
    Left = False
    Right = False
    MISSILE_DELAY = 25
    JUMP_DELAY = 50
    total = 0
    health = games.Text(value=100,
                        size=30,
                        color=color.white,
                        top=65,
                        right=games.screen.width - 710,
                        is_collideable=False)
    games.screen.add(health)
    stone = games.Text(value="Vaporeon",
                       size=30,
                       color=color.blue,
                       top=65,
                       right=games.screen.width - 745,
                       is_collideable=False)
    games.screen.add(stone)

    def __init__(self, x, y):
        """ Initialize Eevee like a boss, and keeps his score."""
        super(Vaporeon, self).__init__(image=Vaporeon.image,  # might be here
                                       x=x, y=y)
        self.missile_wait = 0
        self.jump_wait = 0

    def end(self):
        """Ends game"""
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        Vaporeon.soundend.play()
        games.screen.add(end_message)

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        self.end()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        Eevee.total = 2
        size = 9
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        new_jolteon = Jolteon(x=self.x, y=self.y)
        games.screen.add(new_jolteon)

    def die4(self):
        Eevee.total = 3
        size = 9
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        new_flareon = Flareon(x=self.x, y=self.y)
        games.screen.add(new_flareon)

    def decrease_health(self):
        Vaporeon.health.value -= 10
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def water_evolve(self):
        Vaporeon.stone.value = "Vaporean"

    def update(self):
        """Move and jump around! Just like Eevee in real life!!!"""
        if games.keyboard.is_pressed(games.K_LEFT):
            image2 = games.load_image("vaporeon2.bmp")
            self.set_image(image2)
            Vaporeon.Left = True
            Vaporeon.Right = False
            self.x -= 2
        if games.keyboard.is_pressed(games.K_RIGHT):
            image = games.load_image("vaporeon.png")
            self.set_image(image)
            Vaporeon.Left = False
            Vaporeon.Right = True
            self.x += 2

        if games.keyboard.is_pressed(games.K_UP) and self.jump_wait == 0:
            Vaporeon.sound.play()
            self.jump_wait = Vaporeon.JUMP_DELAY
            self.dy = -4
        if self.bottom < 350:

            self.dy = -self.dy

        if self.top > 390:
            self.dy = 0
            self.y = 400

        if self.top > 400:
            self.dy = 0
            self.y = 400

        # HEALTH
       # if self.overlapping_sprites:
        #    EeveeStats[0] = EeveeStats[0] - 10
         #   Eevee.health.value -= 10
        if self.health.value == 0:
            self.die()

        # Wraps Eevee around screen lol
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        # If waiting until eevee can use Hyper Beam again decrease wait.
        if self.missile_wait > 0:
            self.missile_wait -= 1
        # If waiting until eevee can jum again decrease wait.
        if self.jump_wait > 0:
            self.jump_wait -= 1

        # Use Hyper Beam if spacebar pressed and missile wait is over
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Icebeam(self.x, self.y)
            games.screen.add(new_missile)
            self.missile_wait = Vaporeon.MISSILE_DELAY


class Jolteon(games.Sprite):
    """
    A Jolteon that is ready to fight!
    """
    image = games.load_image("jolteon.bmp")
    sound = games.load_sound("jolteon.wav")
    soundend = games.load_sound("gameover.wav")
    Left = False
    Right = False
    MISSILE_DELAY = 25
    JUMP_DELAY = 50
    total = 0
    health = games.Text(value=100,
                        size=30,
                        color=color.yellow,
                        top=85,
                        right=games.screen.width - 710,
                        is_collideable=False)
    games.screen.add(health)
    stone = games.Text(value="Jolteon",
                       size=30,
                       color=color.yellow,
                       top=85,
                       right=games.screen.width - 745,
                       is_collideable=False)
    games.screen.add(stone)

    def __init__(self, x, y):
        """ Initialize Eevee like a boss, and keeps his score."""
        super(Jolteon, self).__init__(image=Jolteon.image,  # might be here
                                      x=x, y=y)
        self.missile_wait = 0
        self.jump_wait = 0

    def end(self):
        """Ends game"""
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        Vaporeon.soundend.play()
        games.screen.add(end_message)

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        self.end()

    def die2(self):
        Eevee.total = 1
        size = 9
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        new_vaporeon = Vaporeon(x=self.x, y=self.y)
        games.screen.add(new_vaporeon)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        Eevee.total = 3
        size = 9
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        new_flareon = Flareon(x=self.x, y=self.y)
        games.screen.add(new_flareon)

    def decrease_health(self):
        Jolteon.health.value -= 10
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def water_evolve(self):
        Jolteon.stone.value = "Jolteon"

    def update(self):
        """Move and jump around! Just like Eevee in real life!!!"""
        if games.keyboard.is_pressed(games.K_LEFT):
            image2 = games.load_image("jolteon2.bmp")
            self.set_image(image2)
            Jolteon.Left = True
            Jolteon.Right = False
            self.x -= 2
        if games.keyboard.is_pressed(games.K_RIGHT):
            image = games.load_image("jolteon.bmp")
            self.set_image(image)
            Jolteon.Left = False
            Jolteon.Right = True
            self.x += 2

        if games.keyboard.is_pressed(games.K_UP) and self.jump_wait == 0:
            Jolteon.sound.play()
            self.jump_wait = Jolteon.JUMP_DELAY
            self.dy = -4
        if self.bottom < 350:

            self.dy = -self.dy

        if self.top > 390:
            self.dy = 0
            self.y = 400

        if self.top > 400:
            self.dy = 0
            self.y = 400

        # HEALTH
       # if self.overlapping_sprites:
        #    EeveeStats[0] = EeveeStats[0] - 10
         #   Eevee.health.value -= 10
        if self.health.value == 0:
            self.die()

        # Wraps Eevee around screen lol
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        # If waiting until eevee can use Hyper Beam again decrease wait.
        if self.missile_wait > 0:
            self.missile_wait -= 1
        # If waiting until eevee can jum again decrease wait.
        if self.jump_wait > 0:
            self.jump_wait -= 1

        # Use Hyper Beam if spacebar pressed and missile wait is over
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Lightning(self.x, self.y)
            games.screen.add(new_missile)
            self.missile_wait = Jolteon.MISSILE_DELAY


class Flareon(games.Sprite):
    """
    A Flareon that is ready to fight!
    """
    image = games.load_image("flareon.bmp")
    sound = games.load_sound("flareon.wav")
    soundend = games.load_sound("gameover.wav")
    Left = False
    Right = False
    MISSILE_DELAY = 25
    JUMP_DELAY = 50
    total = 0
    health = games.Text(value=100,
                        size=30,
                        color=color.red,
                        top=105,
                        right=games.screen.width - 710,
                        is_collideable=False)
    games.screen.add(health)
    stone = games.Text(value="Flareon",
                       size=30,
                       color=color.red,
                       top=105,
                       right=games.screen.width - 745,
                       is_collideable=False)
    games.screen.add(stone)

    def __init__(self, x, y):
        """ Initialize Eevee like a boss, and keeps his score."""
        super(Flareon, self).__init__(image=Flareon.image,  # might be here
                                      x=x, y=y)
        self.missile_wait = 0
        self.jump_wait = 0

    def end(self):
        """Ends game"""
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        Flareon.soundend.play()
        games.screen.add(end_message)

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        self.end()

    def die2(self):
        Eevee.total = 1
        size = 9
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        new_vaporeon = Vaporeon(x=self.x, y=self.y)
        games.screen.add(new_vaporeon)

    def die3(self):
        Eevee.total = 2
        size = 9
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        new_jolteon = Jolteon(x=self.x, y=self.y)
        games.screen.add(new_jolteon)

    def die4(self):

        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def decrease_health(self):
        Flareon.health.value -= 10
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def water_evolve(self):
        Flareon.stone.value = "Flareon"

    def update(self):
        """Move and jump around! Just like Eevee in real life!!!"""
        if games.keyboard.is_pressed(games.K_LEFT):
            image2 = games.load_image("flareon2.bmp")
            self.set_image(image2)
            Flareon.Left = True
            Flareon.Right = False
            self.x -= 2
        if games.keyboard.is_pressed(games.K_RIGHT):
            image = games.load_image("flareon.bmp")
            self.set_image(image)
            Flareon.Left = False
            Flareon.Right = True
            self.x += 2

        if games.keyboard.is_pressed(games.K_UP) and self.jump_wait == 0:
            Flareon.sound.play()
            self.jump_wait = Flareon.JUMP_DELAY

            self.dy = -4
        if self.bottom < 350:

            self.dy = -self.dy

        if self.top > 390:
            self.dy = 0
            self.y = 400

        if self.top > 400:
            self.dy = 0
            self.y = 400

        # HEALTH
       # if self.overlapping_sprites:
        #    EeveeStats[0] = EeveeStats[0] - 10
         #   Eevee.health.value -= 10
        if self.health.value == 0:
            self.die()

        # Wraps Eevee around screen lol
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        # If waiting until eevee can use Hyper Beam again decrease wait.
        if self.missile_wait > 0:
            self.missile_wait -= 1
        # If waiting until eevee can jum again decrease wait.
        if self.jump_wait > 0:
            self.jump_wait -= 1

        # Use Hyper Beam if spacebar pressed and missile wait is over
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Fireball2(self.x, self.y)
            games.screen.add(new_missile)
            self.missile_wait = Flareon.MISSILE_DELAY


class Mew(games.Sprite):
    """
    A Mew that is ready to fight!
    """
    image = games.load_image("mew.png")
    #sound = games.load_sound("mew.wav")
    soundend = games.load_sound("gameover.wav")
    Left = False
    Right = False
    MISSILE_DELAY = 25
    JUMP_DELAY = 50
    total = 0
    health = 9999

    def __init__(self, x, y):
        """ Initialize Mew like a boss, and keeps his score."""
        super(Mew, self).__init__(image=Mew.image,  # might be here
                                  x=x, y=y)
        self.missile_wait = 0
        self.jump_wait = 0

    def end(self):
        """Ends game"""
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        Flareon.soundend.play()
        games.screen.add(end_message)

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        self.end()

    def die2(self):
        Eevee.total = 1
        size = 9
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        new_vaporeon = Vaporeon(x=self.x, y=400)
        games.screen.add(new_vaporeon)

    def die3(self):
        Eevee.total = 2
        size = 9
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()
        new_jolteon = Jolteon(x=self.x, y=400)
        games.screen.add(new_jolteon)

    def die4(self):

        new_explosion = Explosion(x=self.x, y=400)
        games.screen.add(new_explosion)
        self.destroy()
        new_flareon = Flareon(x=self.x, y=400)
        games.screen.add(new_flareon)

    def decrease_health(self):
        Mew.health -= 10
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def update(self):
        """Move and jump around! Just like Eevee in real life!!!"""
        if games.keyboard.is_pressed(games.K_LEFT):
            image2 = games.load_image("mew2.png")
            self.set_image(image2)
            Mew.Left = True
            Mew.Right = False
            self.dx = -2
        if games.keyboard.is_pressed(games.K_RIGHT):
            image = games.load_image("mew.png")
            self.set_image(image)
            Mew.Left = False
            Mew.Right = True
            self.dx = 2

        if games.keyboard.is_pressed(games.K_UP):
            # Flareon.sound.play()
            self.dy = -2

        if games.keyboard.is_pressed(games.K_DOWN):
            self.dy = 2

        if games.keyboard.is_pressed(games.K_LEFT) and games.keyboard.is_pressed(games.K_RIGHT):
            self.dy = 0
        if games.keyboard.is_pressed(games.K_DOWN) and games.keyboard.is_pressed(games.K_UP):
            self.dx = 0
        # HEALTH
       # if self.overlapping_sprites:
        #    EeveeStats[0] = EeveeStats[0] - 10
         #   Eevee.health.value -= 10
        if self.health <= 0:
            self.die()

        # Wraps Eevee around screen lol
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        # If waiting until eevee can use Hyper Beam again decrease wait.
        if self.missile_wait > 0:
            self.missile_wait -= 1
        # If waiting until eevee can jum again decrease wait.

        # Use Hyper Beam if spacebar pressed and missile wait is over
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Psychic(self.x, self.y)
            games.screen.add(new_missile)
            self.missile_wait = Mew.MISSILE_DELAY


class Water_Stone(games.Sprite):
    """Makes Eevee Evolve"""
    image = games.load_image("waterstone.bmp")
    total = 0
    health = 10

    def __init__(self, game, x, y, speed=1):
        """initialize stone"""
        super(Water_Stone, self).__init__(image=Water_Stone.image,
                                          x=x, y=y, dy=speed)
        x = 200,
        y = 300

    def die(self):
        """Use stone"""
        size = 9
        Water_Stone.total += 1
        for sprite in self.overlapping_sprites:
            sprite.die2()
        self.destroy()

    def decrease_health(self):
        self.health -= 10

    def update(self):
        if self.top < 150:
            dy = 0,
            y = 150
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die2()
            self.destroy()


class Thunder_Stone(games.Sprite):
    """Makes Eevee Evolve"""
    image = games.load_image("thunderstone.bmp")
    total = 0
    health = 10

    def __init__(self, game, x, y, speed=1):
        """initialize stone"""
        super(Thunder_Stone, self).__init__(image=Thunder_Stone.image,
                                            x=x, y=y, dy=speed)
        x = 200,
        y = 300

    def die(self):
        """Use stone"""
        size = 9
        Thunder_Stone.total += 2
        for sprite in self.overlapping_sprites:
            sprite.die3()
        self.destroy()

    def decrease_health(self):
        self.health -= 10

    def update(self):
        if self.top < 150:
            dy = 0,
            y = 150
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die3()
            self.destroy()


class Fire_Stone(games.Sprite):
    """Makes Eevee Evolve"""
    image = games.load_image("firestone.bmp")
    total = 0
    health = 10

    def __init__(self, game, x, y, speed=1):
        """initialize stone"""
        super(Fire_Stone, self).__init__(image=Fire_Stone.image,
                                         x=x, y=y, dy=speed)
        x = 200,
        y = 300

    def die(self):
        """Use stone"""
        size = 9
        Fire_Stone.total += 3
        for sprite in self.overlapping_sprites:
            sprite.die4()
        self.destroy()

    def decrease_health(self):
        self.health -= 10

    def update(self):
        if self.top < 150:
            dy = 0,
            y = 150
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die4()
            self.destroy()


class Missile(games.Sprite):
    """ Eevee getting ready to blow stuff up! """
    image = games.load_image("missile.bmp")
    VELOCITY_FACTOR = 5
    LIFETIME = 40
    BUFFER = 0
    health = 10

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def __init__(self, Eevee_x, Eevee_y):
        # Calculate Hyper Beams starting position
        x = Eevee_x + 100
        y = Eevee_y

        # calculate missile's velocity components
        if Eevee.Right == True:
            dx = 5
            dy = 0
        else:
            x = Eevee_x - 100
            dx = -5
            dy = 0

        super(Missile, self).__init__(image=Missile.image,
                                      x=x, y=y,
                                      dx=dx, dy=dy)
        self.lifetime = Missile.LIFETIME
        if Eevee.Right == True:
            image2 = games.load_image("missile.bmp")
            self.set_image(image2)
            dx = 5
            dy = 0
        else:
            image2 = games.load_image("missile2.bmp")
            self.set_image(image2)
            x = Eevee_x - 100
            dx = -5
            dy = 0

    def decrease_health(self):
        self.health -= 10

    def update(self):
        """Move the Hyperbeam"""
        super(Missile, self).update()

        self.lifetime -= 1

        if self.health == 0:
            self.die()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.decrease_health()
                if sprite.x < self.x:
                    sprite.x -= 25  # this will make sprite fall back when hit
                else:
                    sprite.x += 25
                self.destroy()


class Bubble(games.Sprite):
    """ Eevee getting ready to blow stuff up! """
    image = games.load_image("bubbles.png")
    VELOCITY_FACTOR = 5
    LIFETIME = 40
    health = 10

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def __init__(self, Psyduck_x, Psyduck_y):
        # Calculate Hyper Beams starting position
        x = Psyduck_x
        y = Psyduck_y

        # calculate missile's velocity components
        if Psyduck.Right == True:
            x = Psyduck_x + 100
            y = Psyduck_y
            dx = 5
            dy = 0
        if Psyduck.Left == True:
            x = Psyduck_x - 100
            y = Psyduck_y
            dx = -5
            dy = 0

        super(Bubble, self).__init__(image=Bubble.image,
                                     x=x, y=y,
                                     dx=dx, dy=dy)

        if Psyduck.Right == True:
            image2 = games.load_image("bubbles.png")
            self.set_image(image2)
            dx = 5
            dy = 0
        else:
            image2 = games.load_image("bubbles2.png")
            self.set_image(image2)
            x = Psyduck_x - 100
            dx = -5
            dy = 0

    def decrease_health(self):
        self.health -= 10

        self.lifetime = Bubble.LIFETIME

    def update(self):
        """Move the Hyperbeam"""
        #super(Bubble, self).update()

        if self.health == 0:
            self.die()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.decrease_health()
                if sprite.x < self.x:
                    sprite.x -= 25  # this will make sprite fall back when hit
                else:
                    sprite.x += 25
                self.destroy()


class Bone(games.Animation):
    """ Eevee getting ready to blow stuff up! """
    images = images = ["bone.bmp", "bone.bmp", "bone.bmp", "bone.bmp", "bone.bmp", "bone.bmp",
                       "bone2.bmp", "bone2.bmp", "bone2.bmp", "bone2.bmp", "bone2.bmp", "bone2.bmp"]
    VELOCITY_FACTOR = 5
    LIFETIME = 40
    BUFFER = 0
    health = 10

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def __init__(self, Cubone_x, Cubone_y):
        # Calculate Hyper Beams starting position
        x = Cubone_x - 100
        y = Cubone_y

        # calculate missile's velocity components
        if Cubone.Right == True:
            x = Cubone_x + 100
            y = Cubone_y  # add these
            dx = 5
            dy = 0
        else:
            x = Cubone_x - 100
            dx = -5
            dy = 0

        super(Bone, self).__init__(images=Bone.images,
                                   x=x, y=y,
                                   dx=dx, dy=dy)
        self.lifetime = Bone.LIFETIME

    def decrease_health(self):
        self.health -= 10

    def update(self):
        """Move the Hyperbeam"""
        super(Bone, self).update()

        self.lifetime -= 1

        if self.health == 0:
            self.die()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.decrease_health()
                if sprite.x < self.x:
                    sprite.x -= 25  # this will make sprite fall back when hit
                else:
                    sprite.x += 25
                self.destroy()


class Fireball(games.Sprite):
    """ Eevee getting ready to blow stuff up! """
    image = games.load_image("fireball.bmp")
    VELOCITY_FACTOR = 5
    LIFETIME = 40
    health = 10

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def __init__(self, Charizard_x, Charizard_y):
        # Calculate Hyper Beams starting position
        x = Charizard_x - 100
        y = Charizard_y

        # calculate missile's velocity components
        if Charizard.Right == True:
            x = Charizard_x + 100
            y = Charizard_y
            dx = 5
            dy = 0
        else:
            x = Charizard_x - 100
            dx = -5
            dy = 0

        super(Fireball, self).__init__(image=Fireball.image,
                                       x=x, y=y,
                                       dx=dx, dy=dy)

        if Charizard.Right == True:
            image2 = games.load_image("fireball2.bmp")
            self.set_image(image2)
            dx = 5
            dy = 0
        else:
            image2 = games.load_image("fireball.bmp")
            self.set_image(image2)
            x = Charizard_x - 100
            dx = -5
            dy = 0

    def decrease_health(self):
        self.health -= 10

        self.lifetime = Fireball.LIFETIME

    def update(self):
        """Move the Hyperbeam"""
        #super(Bubble, self).update()

        if self.health == 0:
            self.die()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.decrease_health()
                if sprite.x < self.x:
                    sprite.x -= 25  # this will make sprite fall back when hit
                else:
                    sprite.x += 25
                self.destroy()


class Shadowball(games.Sprite):
    """ Eevee getting ready to blow stuff up! """
    image = games.load_image("shadowball.bmp")
    VELOCITY_FACTOR = 5
    LIFETIME = 40
    health = 10

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def __init__(self, Mewtwo_x, Mewtwo_y):
        # Calculate Hyper Beams starting position
        x = Mewtwo_x - 100
        y = Mewtwo_y

        # calculate missile's velocity components
        if Mewtwo.Right == True:
            x = Mewtwo_x + 100
            y = Mewtwo_y
            dx = 5
            dy = 0
        else:
            x = Mewtwo_x - 100
            dx = -5
            dy = 0

        super(Shadowball, self).__init__(image=Shadowball.image,
                                         x=x, y=y,
                                         dx=dx, dy=dy)

    def decrease_health(self):
        self.health -= 10

        self.lifetime = Shadowball.LIFETIME

    def update(self):
        """Move the Hyperbeam"""
        #super(Bubble, self).update()

        if self.health == 0:
            self.die()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.decrease_health()
                if sprite.x < self.x:
                    sprite.x -= 25  # this will make sprite fall back when hit
                else:
                    sprite.x += 25
                self.destroy()


class Icebeam(games.Sprite):
    """ Eevee getting ready to blow stuff up! """
    image = games.load_image("icebeam.bmp")
    VELOCITY_FACTOR = 5
    LIFETIME = 40
    health = 10

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def __init__(self, Vaporeon_x, Vaporeon_y):
        # Calculate Hyper Beams starting position
        x = Vaporeon_x + 100
        y = Vaporeon_y

        # calculate missile's velocity components
        if Vaporeon.Right == True:
            dx = 5
            dy = 0
        else:
            x = Vaporeon_x - 100
            dx = -5
            dy = 0

        super(Icebeam, self).__init__(image=Icebeam.image,
                                      x=x, y=y,
                                      dx=dx, dy=dy)
        if Vaporeon.Right == True:
            image2 = games.load_image("icebeam.bmp")
            self.set_image(image2)
            dx = 5
            dy = 0
        else:
            image2 = games.load_image("icebeam.png")
            self.set_image(image2)  # left needs to face opposite direction
            x = Vaporeon_x - 100
            dx = -5
            dy = 0

    def decrease_health(self):
        self.health -= 10

        self.lifetime = Icebeam.LIFETIME

    def update(self):
        """Move the Hyperbeam"""
        #super(Bubble, self).update()

        if self.health == 0:
            self.die()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.decrease_health()  # left wrong right huge
                if sprite.x < self.x:
                    sprite.x -= 25  # this will make sprite fall back when hit
                else:
                    sprite.x += 25
                self.destroy()


class Psychic(games.Sprite):
    """ Mew getting ready to blow stuff up! """
    image = games.load_image("psychic.png")
    VELOCITY_FACTOR = 15
    LIFETIME = 40
    health = 10

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def __init__(self, Mew_x, Mew_y):
        # Calculate Hyper Beams starting position
        x = Mew_x + 100
        y = Mew_y

        # calculate missile's velocity components
        if Mew.Right == True:
            dx = 5
            dy = 0
        else:
            x = Mew_x - 100
            dx = -5
            dy = 0

        super(Psychic, self).__init__(image=Psychic.image,
                                      x=x, y=y,
                                      dx=dx, dy=dy)

    def decrease_health(self):
        self.health -= 10

        self.lifetime = Icebeam.LIFETIME

    def update(self):
        """Move the Hyperbeam"""
        super(Psychic, self).update()

        if self.health == 0:
            self.die()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.decrease_health()
                sprite.decrease_health()
                sprite.decrease_health()
                sprite.decrease_health()
                sprite.decrease_health()
                if sprite.x < self.x:
                    sprite.x -= 150  # this will make sprite fall back when hit
                else:
                    sprite.x += 25
                self.destroy()


class Lightning(games.Sprite):
    """ Eevee getting ready to blow stuff up! """
    image = games.load_image("lightning.bmp")
    VELOCITY_FACTOR = 5
    LIFETIME = 40
    health = 10

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def __init__(self, Jolteon_x, Jolteon_y):
        # Calculate Hyper Beams starting position
        x = Jolteon_x + 100
        y = Jolteon_y

        # calculate missile's velocity components
        if Jolteon.Right == True:
            dx = 5
            dy = 0
        else:
            x = Jolteon_x - 100
            dx = -5
            dy = 0

        super(Lightning, self).__init__(image=Lightning.image,
                                        x=x, y=y,
                                        dx=dx, dy=dy)

    def decrease_health(self):
        self.health -= 10

        self.lifetime = Lightning.LIFETIME

    def update(self):
        """Move the Hyperbeam"""
        #super(Bubble, self).update()

        if self.health == 0:
            self.die()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.decrease_health()
                if sprite.x < self.x:
                    sprite.x -= 25  # this will make sprite fall back when hit
                else:
                    sprite.x += 25
                self.destroy()


class Fireball2(games.Sprite):
    """ Eevee getting ready to blow stuff up! """
    image = games.load_image("fireball2.bmp")
    VELOCITY_FACTOR = 5
    LIFETIME = 40
    health = 10

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()

    def die2(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die3(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def die4(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)

    def __init__(self, Flareon_x, Flareon_y):
        # Calculate Hyper Beams starting position
        x = Flareon_x + 100
        y = Flareon_y

        # calculate missile's velocity components
        if Flareon.Right == True:
            dx = 5
            dy = 0
        else:
            x = Flareon_x - 100
            dx = -5
            dy = 0

        super(Fireball2, self).__init__(image=Fireball2.image,
                                        x=x, y=y,
                                        dx=dx, dy=dy)

        if Flareon.Right == True:
            image2 = games.load_image("fireball2.bmp")
            self.set_image(image2)
            dx = 5
            dy = 0
        else:
            image2 = games.load_image("fireball.bmp")
            self.set_image(image2)
            x = Flareon_x - 100
            dx = -5
            dy = 0

    def decrease_health(self):
        self.health -= 10

        self.lifetime = Fireball2.LIFETIME

    def update(self):
        """Move the Hyperbeam"""
        #super(Bubble, self).update()

        if self.health == 0:
            self.die()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.decrease_health()
                if sprite.x < self.x:
                    sprite.x -= 25  # this will make sprite fall back when hit
                else:
                    sprite.x += 25
                self.destroy()


class Explosion(games.Animation):
    """ Explosion animation. """
    sound = games.load_sound("boom.wav")
    images = ["explosion1.bmp",
              "explosion2.bmp",
              "explosion3.bmp",
              "explosion4.bmp",
              "explosion5.bmp",
              "explosion6.bmp",
              "explosion7.bmp",
              "explosion8.bmp",
              "explosion9.bmp"]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images=Explosion.images,
                                        x=x, y=y,
                                        repeat_interval=4, n_repeats=1,
                                        is_collideable=False)
        Explosion.sound.play()


class Game(object):
    """Setting up this boss game"""

    def __init__(self):
        """Initialize Game Object"""
        # sets level
        self.level = 0

        # put sound here
        self.sound = games.load_sound("psyduck.wav")

        # health here
        """self.health = games.Text(value = 100,
                                 size = 30,
                                 color = color.red,
                                 top = 5,
                                 right = games.screen.width - 10,
                                 is_collideable = False)
        games.screen.add(self.health)"""

        # Create Eevee
        self.Eevee = Eevee(x=100,
                           y=400)
        games.screen.add(self.Eevee)

        # Create Psyduck
        self.Psyduck = Psyduck(game=self,
                               x=600,
                               y=400)
        games.screen.add(self.Psyduck)
        self.sound.play()

        # Create Cubone
        if Psyduck.total == 0:  # Make Charizard or Blastoise or snorlax
            self.cubone = Cubone(game=self,
                                 x=600,
                                 y=400)
            games.screen.add(self.Cubone)

        # Create Charizard
        if Psyduck.total == 0 and Cubone.total == 0:  # Make Charizard
            self.charizard = Charizard(game=self,
                                       x=600,
                                       y=400)
            games.screen.add(self.Charizard)
        # Create Snorlax
        if Psyduck.total == 0 and Cubone.total == 0 and Charizard.total == 0:  # Make Snorlax
            self.snorlax = Snorlax(game=self,
                                   x=600,
                                   y=400)
            games.screen.add(self.Snorlax)
        # Create Mewtwo
        if Psyduck.total == 0 and Cubone.total == 0 and Charizard.total == 0 and Snorlax.total:  # Make Snorlax
            self.mewtwo = Mewtwo(game=self,
                                 x=600,
                                 y=400)
            games.screen.add(self.Mewtwo)
        # Evolve into Vaporeon
        if Eevee.total == 1:
            self.vaporeon = Vaporeon(x=200,
                                     y=400)
            games.screen.add(self.vaporeon)

        # Evolve into Jolteon
        if Eevee.total == 2:
            self.jolteon = Jolteon(x=200,
                                   y=400)
            games.screen.add(self.jolteon)

        # Evolve into Flareon
        if Eevee.total == 3:
            self.flareon = Flareon(x=200,
                                   y=400)
            games.screen.add(self.flareon)

        if Eevee.total == 4:
            self.mew = Mew(x=200,
                           y=400)

        # randomize stones
        if Psyduck.stone == 0:
            Psyduck.total = random.randint(1, 3)
        # Create Waterstone
            if Psyduck.stone == 1:
                self.waterstone = Water_Stone(game=self,
                                              x=400,
                                              y=2)
                games.screen.add(self.waterstone)
        # Create thunderstone
            if Psyduck.stone == 2:
                self.thunderstone = Thunder_Stone(game=self,
                                                  x=300,
                                                  y=2)
                games.screen.add(self.thunderstone)
        # Create Firestone
            if Psyduck.stone == 3:

                self.firestone = Fire_Stone(game=self,
                                            x=200,
                                            y=2)
                games.screen.add(self.firestone)

    def play(self):
        """ Play game """

        # music
        games.music.load("clocks.mid")
        games.music.play(-100)  # ENABLE THIS BEFORE TURNING IN!!!

        # load and set background
        armory_image = games.load_image("armory.jpg")
        games.screen.background = armory_image

        # start it up
        games.screen.mainloop()

    def end(self):
        """ End the game. """
        # show 'Game Over' for 5 seconds
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        games.screen.add(end_message)

    def win(self):
        """ End the game win. """
        # show 'Game Over' for 5 seconds
        end_message = games.Message(value="You Win!",
                                    size=90,
                                    color=color.blue,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        games.screen.add(end_message)


def main():
    pokekombat = Game()
    pokekombat.play()

main()
