import pygame
import gamesetting as gs

class Assets:
    def __init__(self):
        self.sprite_sheet = self.load_sprite_sheet("images", "BombermanLandPSP-Bomberman.png", 192*4, 272*4)
        self.player_char = self.load_sprite_range(gs.PLAYER, self.sprite_sheet)

    def load_sprite_sheet(self, path, file_name, width, height):
        """Load a sprite sheet and split it into individual sprites.""" 
        image = pygame.image.load(f"{path}/{file_name}").convert_alpha()
        image = pygame.transform.scale(image, (width, height))
        return image
    
    def load_sprites(self, spritesheet, xcoord, ycoord, width, height):
        """Load individual sprites from a sprite sheet."""
        # CREATE AN EMPTY SURFACE
        image = pygame.Surface((width, height))
        # Fill the surface with a off color
        image.fill((0, 0, 1))
        # BLIT THE SPRITE SHEET ONTO THE NEW SURFACE
        image.blit(spritesheet, (0, 0), (xcoord, ycoord, width, height))
        # CONVERT BLACK COLOURS ON THE NEW IMAGE TO TRANSPARENT 
        image.set_colorkey(gs.BLACK)
        return image
    
    def load_sprite_range(self, image_dict, spritesheet, row=gs.SIZE, col=gs.SIZE, width=gs.SIZE, height=gs.SIZE, resize=False):
        """Return a dictionary containing list of images for the animation."""
        animation_images = {}
        for animation in image_dict.keys():
            animation_images[animation] = []
            for coord in image_dict[animation]:
                image = self.load_sprites(spritesheet, coord[1] * col, coord[0] * row, width, height)
                if resize:
                    image = pygame.transform.scale(image, (32, 32))
                animation_images[animation].append(image)
        return animation_images
