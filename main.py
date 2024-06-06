import time,os,sys

class Game:
    def __init__(self):
        self.locations = {
            'cell': '\n''You are in a small, dark, and damp cell. Rusted bars enclose you, and a faint smell of mold lingers in the air.',
            'hallway': '\n''You are in a dimly lit hallway. Overhead lights flicker, and peeling paint covers the walls. Debris litters the floor, and dried bloodstains mar the surface.',
            'warden_office': '\n''You are in a a large room with a heavy wooden desk and overturned filing cabinets. Papers are scattered everywhere, and a crooked portrait of the former warden hangs on the wall.',
            'dock': '\n''You are in a decrepit wooden dock overlooking the rough sea.',
            'lab': '\n''You are in a sterile, clinical room filled with broken equipment and the smell of chemicals.',
            'chapel': '\n''You are in a dilapidated chapel, with broken pews and shattered stained glass windows.',
            'forest': '\n''You are in a dense, overgrown forest surrounding the prison. Twisted trees and thick underbrush obscure the path ahead.',
            'entrance': '\n' 'You are in the main entrance of the prison. The large iron gates are partially open, rusted from years of neglect.',
            'tool_shed': '\n' 'The small space is cluttered with rusty tools, old cans of paint, and various other items.'
        }

        self.lookaround = {
            'cell': '\n''The walls are covered in graffiti, each message more cryptic than the last. Scratch marks line the lower part of the walls, suggesting someone tried to claw their way out. The damp air is thick with the smell of mold and decay. The [bunk bed] is old and creaks with any movement, the [toilet] is rusted and unsanitary, and the small [window] high up on the wall is barred, allowing a sliver of moonlight to pierce through the gloom.',
            'hallway': '\n''The dim light casts eerie shadows, making the peeling paint and debris appear even more menacing. As your eyes scan the [doors] lining the hallway, you notice some are slightly open while others remain firmly shut. The [stairs] at the far end lead to the Warden\'s Office. [Graffiti] on the walls seems to shift and writhe in the flickering light.',
            'warden_office': '\n''The room is filled with an air of neglect and decay. Papers cover the floor, most of them yellowed and brittle with age. The [desk drawer] is slightly ajar, and you can see a glint of metal inside. The [safe] in the corner is covered in dust, and its combination lock is firmly in place. The [portrait] of the former warden hangs crooked on the wall, its eyes seeming to follow you as you move.',
            'dock': '\n''You look around the dock. The wooden planks beneath your feet are weathered and unstable, creaking with each step. The [boat] tied up nearby looks worn but potentially seaworthy. A small tool shed sits at the edge of the dock. Carved into the wood of the dock are [clues], left behind by those who came before you, hinting at the dangers and secrets of the island.',
            'lab': '\n''The laboratory is a grim sight. Broken glass and shattered equipment litter the floor, while the smell of chemicals lingers in the air. Research notes cover the walls, detailing horrific and unethical experiments conducted here. The centerpiece is a grimy [operating table], stained and surrounded by broken instruments. To one side, a [locked cabinet] stands, its door tightly secured. The [experiment logs] scattered around the room are filled with disturbing details.',
            'chapel': '\n''The chapel is a haunting sight. The once-grand stained glass windows are now shattered, their colorful pieces strewn across the floor. The [altar] at the front of the chapel is covered in a thick layer of dust, with a few flickering candles providing the only light. To one side, the [confessional booth] stands ominously, its door slightly ajar. The walls are adorned with a disturbing [mural] depicting scenes of punishment and suffering.',
            'forest': '\n''You look around the forest. The forest is dense and foreboding, with towering trees and tangled undergrowth blocking out much of the light. Strange sounds echo through the trees, and the air feels heavy with tension. An abandoned [campsite] dot the landscape, remnants of previous escape attempts. You also notice a [pit] partially concealed by leaves, something shiny at the bottom catches your eye.',
            'entrance': '\n' 'You look around the entrance. The imposing iron gates stand as a silent reminder of the prison’s past. The gatehouse, now abandoned and overgrown, still has remnants of its former use. Broken glass crunches underfoot, and old security cameras hang uselessly from their mounts. Graffiti covers the walls, some of it old and faded, while other pieces seem more recent, possibly from other survivors or explorers who dared to come this way.',
            'tool_shed': '\n' 'You look around the tool shed. The room is filled with tools and supplies, some scattered haphazardly on the floor. A [workbench] against one wall is piled with various mechanical parts and tools. A [toolbox] sits underneath the bench, partially hidden from view. You also notice a [hidden compartment] in the floorboards, slightly raised and out of place.'
        }
        self.current_location = 'cell'
        self.truth = False
        self.clues = {
            'cell': False,
            'hallway': False,
            'warden_office': False,
            'dock': False,
            'lab': False,
            'chapel': False,
            'forest': False,
            'tool_shed': False
        }
        self.puzzles = {
            'cell': False,
            'hallway': False,
            'warden_office': False,
            'dock': False,
            'lab': False,
            'chapel': False,
            'forest': False,
            'tool_shed': False
        }
        self.locked = {
            'cell': False,
            'hallway': False,
            'warden_office': False,
            'dock': True,
            'lab': True,
            'lab_locker': True,
            'chapel': False,
            'forest': False,
            'tool_shed': True
        }
        self.endings = {
            'true': False,
            'good': False,
            'bad': False
        }
        self.first_time = {
            'cell': False,
            'hallway': True,
            'warden_office': True,
            'dock': True,
            'lab': True,
            'chapel': True,
            'forest': True,
            'entrance': True,
            'tool_shed': True
        }
        self.game_over = False

#Start Game Function
    def start(self):
        os.system("clear")
        print('\n'"Welcome to 'Forgotten Memories'. A game by Danilo Pereira"'\n')
        
        while not self.game_over:
            self.check_ending()
            print(self.locations[self.current_location])
            print('\n'"[look] [interact] [move] ")
            command = input("> ").strip().lower()
            os.system("clear")
            self.process_command(command)

#General Commands
    def process_command(self, command):
        if command == 'look':
            self.look()
        elif command == 'quit': #debug: quit
            self.game_over = True   
        elif command == 'clues': #debug: check all clues
            print(self.clues)
        elif command == 'current': #debug: check location
            print(self.current_location)      
        elif command == 'first': #debug: check first time in location
            print(self.first_time)
        elif command == 'end': #debug: check endings status
            print(self.endings)    
        elif command == 'debug': #debug:go to True ending conditions
            self.clues = {
            'cell': True,
            'hallway': True,
            'warden_office': True,
            'dock': True,
            'lab': True,
            'chapel': True,
            'forest': True,
            'tool_shed': True
        }
        elif command == 'move':
            self.move(command)
        elif command == 'interact':
            self.interact(command)
        else:
            print('You can\'t do that here')


#Look function
    def look(self):
        if self.current_location == 'hallway' and self.first_time['hallway'] == True:
            print(self.lookaround[self.current_location])
            print('\n''Suddenly, your vision blurs, and you feel a cold shiver run down your spine. The walls close in, the lights flicker faster, and you see shadowy figures moving towards you, their faces twisted in silent screams. The sensation is overwhelming, and just as quickly as it started, it stops. You blink, and the hallway is still once more, the figures gone. A deep sense of unease lingers.')
            self.first_time['hallway'] = False      
        else:
            print(self.lookaround[self.current_location])



#Interact Funtion
    def interact(self,command):  
    #Interact commands in Cell
        if command == 'interact':
            print('\n'"What do you want to interact?")
            interaction = input("> ").strip().lower()
            if interaction == 'bunk bed' and self.current_location == 'cell':
                print('\n''You approach the bunk bed. It looks old and fragile, the metal frame creaking as you touch it. As you examine it more closely, you notice something scratched into the underside of the top bunk. It\'s a message: "Seek the warden’s office. The truth lies within." This cryptic clue sends a shiver down your spine, hinting at something crucial about your past and the reason you’re here.')
                self.clues['cell'] = True
            elif interaction == 'toilet' and self.current_location == 'cell':
                print('\n''You inspect the toilet. It\'s as unsanitary as you expected, rusted and barely functional. There\'s nothing here that could help you understand your situation or aid in your escape.')
            elif interaction == 'window' and self.current_location == 'cell':
                print('\n''You look up at the small window. The bars are firmly in place, and the window itself is too high to reach without something to stand on. The moonlight filtering through provides a tiny bit of light, but there\'s no way to escape through it.')
            
    #Interact commands in Hallway
            elif interaction == 'doors' and self.current_location == 'hallway':
                print('\n''You approach one of the [doors]. The wood is splintered, and the handle feels cold and grimy. Pushing it open slightly, you peer inside to find another empty cell, identical to the one you just left. It seems like a dead end.')
            elif interaction == 'stairs' and self.current_location == 'hallway':
                print('\n''You walk over to the [stairs]. The metal steps are rusted and creak ominously under your weight. Looking up, you see the way is blocked by debris, making it impassable. However, the way down is clear, leading to the Warden\'s Office. A sense of foreboding warns you to be cautious.')
            elif interaction == 'graffiti' and self.current_location == 'hallway':
                print('\n''You examine the [graffiti] more closely. The symbols and words scrawled on the walls seem random at first, but as you focus, you notice a pattern. One section stands out, a repeated phrase: "The truth is buried." Below it, an arrow points towards the Warden\'s Office. Among the chaotic scribbles, you also find a name etched deeply into the paint: "Harrison." It triggers a faint memory, but it\'s just out of reach.')
                self.clues['hallway'] = True
   
    #Interact commands in Warden's Office
            elif interaction == 'desk drawer' and self.current_location == 'warden_office' and self.first_time['warden_office'] == True:
                print('\n''You pull open the [desk drawer] fully. Inside, you find a few old documents and a rusted key. As you reach for the key, a cold draft sweeps through the room, and you hear a whispering voice behind you. Turning quickly, you see shadowy figures crowding the room, their mouths open in silent screams. The room spins, and you feel as if you\'re falling. You blink, and the hallucination vanishes. The room is as it was, but the sense of unease remains.')
                self.first_time['warden_office'] = False
                self.locked['lab_locker'] = False
            elif interaction == 'desk drawer' and self.current_location == 'warden_office':
                print('\n''The desk drawer is empty.')
            elif interaction == 'portrait' and self.current_location == 'warden_office':
                print('\n''You straighten the [portrait] on the wall, noticing something odd. There are numbers faintly scratched into the frame: 4-2-9. You realize this could be the combination for the safe.')
                self.puzzles['warden_office'] = True
            elif interaction == 'safe' and self.current_location == 'warden_office' and self.puzzles['warden_office'] == False:
                print('\n''The [safe] stands resolute in the corner, its combination lock demanding a code. You remember the graffiti in the hallway: "The truth is buried." Perhaps the answer lies hidden in the room.')
            elif interaction == 'safe' and self.current_location == 'warden_office' and self.puzzles['warden_office'] == True:
                print('\n''You enter the combination into the safe. With a click, the safe door swings open. Inside, you find an old journal. Flipping through it, you discover detailed accounts of the prison\'s history and some disturbing entries about experiments conducted on prisoners. One entry stands out: a note about "Harrison" and a hidden passage beneath the chapel.')
                self.clues['warden_office'] = True

    #Interact commands in Chapel 
            elif interaction == 'altar' and self.current_location == 'chapel' and self.endings['true'] == True:
                print('\n''You approach the [altar], the faint whispers of your past growing louder in your mind. As you touch the cold stone, a final, overwhelming hallucination takes hold.')
                print('\n''The world around you blurs and shifts. You find yourself standing in the pristine laboratory, no longer abandoned and broken, but in its prime. The other scientists bustle around, their faces familiar yet distant. Your own face stares back at you from a reflective surface, not with the confusion and fear you now feel, but with determination and purpose.')
                print('\n''Past Self: "We had to do it. A deadly disease was spreading, and the prisoners were the only available subjects. Their lives were already condemned, and we believed we could save millions. The experiments were necessary, a means to an end. But it all went wrong."')
                print('\n''Flashes of the experiments flood your mind—the prisoners\' faces twisted in pain, their bodies suffering from the tests. Among them, you see a familiar face, twisted not by the experiments, but by grief and guilt.')
                print('\n''Past Self: "It was our fault. My fault. We lost control. The inmates revolted, and the island became a nightmare. I tried to cover it up, erase the evidence, but I couldn\'t escape my own conscience. I left clues, hoping someone would find them, understand, and see the bigger picture."')
                print('\n''The hallucination shifts again. You see the chapel filled with people—guards, inmates, scientists—all looking towards you. Their faces are accusing, but also pleading. Your past self steps forward once more.')
                print('\n''Past Self: "We discovered too late that the disease was a false alarm, a misdiagnosis. All our actions, all the suffering, were in vain. It was this realization, this overwhelming guilt, that caused the memory loss. You couldn\'t live with the truth."')
                print('\n''You snap back to reality, the chapel once again silent and eerie. The final pieces of the puzzle fall into place. You were not just a participant in the experiments, but one of their architects. The weight of your actions settles heavily on your shoulders. The truth is a heavy burden, and it all comes crashing down on you.')
                self.truth = True
            elif interaction == 'altar' and self.current_location == 'chapel':
                print('\n''You approach the [altar], noticing an old, dusty book lying atop it. Opening the book, you find it filled with religious texts and rituals. A folded piece of paper falls out from between the pages. Unfolding it, you discover a note: "Seek redemption where sins are confessed, and the truth will be revealed." This seems to hint at the confessional booth.')    
            elif interaction == 'confessional booth' and self.current_location == 'chapel' and self.first_time['chapel'] == True:
                print('\n''You step into the [confessional booth], the wooden door creaking as you close it behind you. Sitting in the dim light, you hear a voice whisper from the other side of the screen, "I know your sins. You cannot hide from them." The voice fades, leaving you with a chilling sense of dread. This cryptic message seems to suggest that the chapel holds more secrets.')
                self.first_time['chapel'] = False
                self.clues['chapel'] = True
            elif interaction == 'confessional booth' and self.current_location == 'chapel':
                print('\n''The confessional booth is empty, but you still remember the voice talking to you.')
            elif interaction == 'mural' and self.current_location == 'chapel' and self.clues['warden_office'] == True:
                print('\n''You remember the entry you found in the Warden\'s Office and examine the [mural] closely, tracing your fingers over the disturbing scenes. One section of the mural seems different, as if it\'s a door painted to blend in with the artwork. Pushing on it, you hear a click, and the mural swings open, revealing a hidden passage leading to the laboratory.')
                self.locked['lab'] = False
            elif interaction == 'mural' and self.current_location == 'chapel' and self.clues['warden_office'] == False:
                print('\n''A disturbing mural that depicts scenes of punishment and suffering. You feel like there is some greater meaning to it. Maybe you\'re missing something.')
                
    #Interact commands in Lab
            elif interaction == 'operating table' and self.current_location == 'lab':
                print('\n''You approach the [operating table], the stains and broken instruments around it painting a picture of the horrors that took place here. As you examine it, you find a small bottle with a mysterious substance.')
                print('\n''Do you want to interact with this substance?')
                decision = input("> ").strip().lower()
                if decision == 'yes' and self.current_location == 'lab':
                    self.end_game('bad')
                elif decision == 'no' and self.current_location == 'lab':
                    print('\n''You decide it\'s best to leave the mysterious substance alone. You place the bottle back on the table and continue your search.')
            elif interaction == 'experiment logs' and self.current_location == 'lab':
                print('\n''You sift through the [experiment logs], reading about the horrific experiments conducted here. The logs detail procedures that were meant to find some kind of cure. One log stands out, mentioning the [locked cabinet] and hinting at critical information inside it.')
            elif interaction == 'locked cabinet' and self.current_location == 'lab' and self.locked['lab_locker'] == True:
                print('\n''The cabinet is tightly locked. The key is probably still somewhere on the island. More investigation will be required before you can open the lock.')
            elif interaction == 'locked cabinet' and self.current_location == 'lab' and self.locked['lab_locker'] == False:
                print('\n''You approach the [locked cabinet], its door tightly secured. You recall the rusted key found in the Warden’s office. You insert the key into the lock, and with some effort, the cabinet creaks open, revealing a photograph of you with a laboratory team, along with several reports written by you. The reports detail the experiments conducted here, including your direct involvement.')
                self.clues['lab'] = True
                self.first_time['lab'] = False
            elif interaction == 'locked cabinet' and self.current_location == 'lab' and self.locked['lab_locker'] == False and self.first_time['lab'] == False:
                print('\n''The cabinet is empty.')
   
    #Interact commands in Forest
            elif interaction == 'campsite' and self.current_location == 'forest':
                print('\n''You approach an abandoned [campsite], its fire pit long since cold and tents in tatters. Among the debris, you find a weathered diary. Flipping through the pages, you come across an entry written by one of the prisoner:')
                print('\n''"Day 12.' '\n' 'We\'re running out of time. The others are getting desperate. Every night we hear them...the scientists. They said they were trying to help, but the things they did... it was torture.') 
                print('One of them, the one with the cold eyes, seemed to take pleasure in our pain. I think he was the one in charge. Last night, we tried to make a break for it. Jerry thought he saw a way out near the north cliffs, but he was wrong. The screams still echo in my ears.') 
                print('We have to avoid the guards and the scientists at all costs. If they catch us, we\'re done for.') 
                print('If anyone finds this, know that we tried. Know that we didn\'t go down without a fight. And if you see the scientists... run."')
                self.clues['forest'] = True
            elif interaction == 'pit' and self.current_location == 'forest':  
                print('\n''You encounter a [pit], a treacherous trap hidden beneath a thick layer of leaves. At the bottom, you see a shining key.')  
                print('\n''Do you want to go down to retrieve the key?')
                decision = input("> ").strip().lower()
                if decision == 'yes' and self.current_location == 'forest':
                    print('\n''Do you want to go down [carefully] or just [jump]?')
                    decision2 = input("> ").strip().lower()
                    if decision2 == 'carefully' and self.current_location == 'forest':
                        self.end_game('bad')
                    elif decision2 == "jump" and self.current_location == 'forest':
                        print('\n''You take a leap of faith and jump into the pit. To your surprise, the pit is not very deep, and you land safely at the bottom. You pick up the key, realizing that fear had distorted your perception.')
                        self.locked['tool_shed'] = False
                elif decision == 'no' and self.current_location == 'forest':
                    print('\n''You decide not to risk going down into the pit. The key remains at the bottom, out of reach, and you move on with a sense of lingering doubt about what the key might unlock.')
   
    #Interact commands in Dock
            elif interaction == 'boat' and self.current_location == 'dock' and self.locked['dock'] == True: 
                print('\n''You approach the [boat], noticing it needs some repairs before it can be used to escape. The hull has a few holes, and the engine looks like it hasn\'t been started in years. Nearby, you see a list of needed repairs and supplies.')
                print('\n''Do you want to try to escape the island without fixing the boat?')
                decision = input("> ").strip().lower()
                if decision == 'yes' and self.current_location == 'dock':
                    self.end_game('bad')
                elif decision == 'no' and self.current_location == 'dock':
                    print('\n''You realize that attempting to escape without proper repairs would be suicide. You decide to search for the necessary tools and materials instead.')
            elif interaction == 'boat' and self.current_location == 'dock' and self.locked['dock'] == False and self.endings['true'] == True and self.truth == True:
                    print('\n''You have gathered all the clues scattered across the island, and the full weight of the truth now presses upon you. As you stand on the dock, the boat ready to take you away, you realize that you have a FINAL choice to make: [leave] the island and live with the guilt, or [stay] and face the consequences of your actions.')
                    decision2 = input("> ").strip().lower()
                    if decision2 == 'leave' and self.current_location == 'dock' and self.endings['true'] == True and self.truth == True:
                        self.end_game('true')
                    elif decision2 == 'stay' and self.current_location == 'dock' and self.endings['true'] == True and self.truth == True:
                        self.end_game('atonement')
            elif interaction == 'boat' and self.current_location == 'dock' and self.locked['dock'] == False:
                print('\n''You have managed to repair the boat using the tools and repair kit you found in the tool shed. The sea is calm, and the moonlight casts a serene glow over the water.')
                print('\n''Are you ready to leave?') 
                decision = input("> ").strip().lower()      
                if decision == 'yes' and self.current_location == 'dock' and self.endings['good'] == True:
                    self.end_game('good')
                elif decision == 'no' and self.current_location == 'dock':
                    print('\n''You decide to step back and investigate the island a little bit more')
            elif interaction == 'clues' and self.current_location == 'dock':
                print('\n''You examine the [clues] carved into the wood. They are messages from previous prisoners or survivors, warning about the treacherous waters and giving tips on how to escape. One message catches your eye: "Find the hidden compartment in the tool shed – it holds the key to your freedom."')
                self.clues['dock'] = True
    
    #Interact commands in Tool Shed
            elif interaction == 'workbench' and self.current_location == 'tool_shed': 
                print('\n''You approach the [workbench], examining the various tools and parts. Most of it looks old and worn, but you find a few useful items that could help in repairing the boat. Among the clutter, you notice a small, dusty box with wires and bolts.')
            elif interaction == 'toolbox' and self.current_location == 'tool_shed': 
                print('\n''You pull out the [toolbox] from under the bench. Opening it, you find a comprehensive set of tools, including wrenches, pliers, and screwdrivers. More importantly, you find a repair kit specifically for boat engines. This is exactly what you need to fix the boat.')
                self.locked['dock'] = False
                self.endings['good'] = True
            elif interaction == 'hidden compartment' and self.current_location == 'tool_shed': 
                print('\n''You pry open the [hidden compartment] in the floorboards. Inside, you find a small, old-fashioned tape recorder with a cassette tape labeled "Project Justification." Intrigued, you press play and listen to the recording. The recording crackles to life, and you hear your own voice, filled with determination and desperation:')
                print('\n''"This is Dr. John Harrison. If you\'re hearing this, it means everything has gone wrong. The experiments were supposed to save lives, not destroy them. We were working on a cure for a deadly disease that was spreading rapidly. Using prisoners was our only option—they were considered expendable by the government, and we were running out of time. But something went wrong. The serum caused violent reactions, turning them into something monstrous. I thought I could control it, reverse the effects, but I was wrong. If you\'re hearing this, please, forgive me. I was only trying to help."')
                self.clues['tool_shed'] = True
            else:
                print('\n'"Invalid command or you can't do that here.")
    



#Move Function
    def move(self,command):
    #Move commands in Cell
        if command == 'move': 
            print('\n'"Where do you want to move? [north] [east] [south] [west]")
            direction = input("> ").strip().lower()
            if direction == 'east' and self.current_location == 'cell':
                self.current_location = 'hallway'
            
    #Move commands in Hallway
            elif direction == 'south' and self.current_location == 'hallway':
                self.current_location = 'entrance'
            elif direction == 'west' and self.current_location == 'hallway':
                self.current_location = 'cell'
            elif direction == 'north' and self.current_location == 'hallway':
                self.current_location = 'warden_office'
            elif direction == 'east' and self.current_location == 'hallway':
                self.current_location = 'chapel'
    
    #Move commands in Warden's
            elif direction == 'south' and self.current_location == 'warden_office':
                self.current_location = 'hallway'

    #Move commands in Chapel
            elif direction == 'west' and self.current_location == 'chapel':
                self.current_location = 'hallway'
            elif direction == 'east' and self.current_location == 'chapel' and self.locked['lab'] == True:
                print('\n''You feel a light breeze coming from that direction, but there is no entrance.')
            elif direction == 'east' and self.current_location == 'chapel' and self.locked['lab'] == False:
                self.current_location = 'lab'

    #Move commands in Lab
            elif direction == 'west' and self.current_location == 'lab':
                self.current_location = 'chapel'

    #Move commands in Entrance
            elif direction == 'north' and self.current_location == 'entrance':
                self.current_location = 'hallway'
            elif direction == 'east' and self.current_location == 'entrance':
                self.current_location = 'dock'
            elif direction == 'south' and self.current_location == 'entrance':
                self.current_location = 'forest'

    #Move commands in Forest
            elif direction == 'north' and self.current_location == 'forest':
                self.current_location = 'entrance'

    #Move commands in Dock        
            elif direction == 'west' and self.current_location == 'dock':
                self.current_location = 'entrance'
            elif direction == 'east' and self.current_location == 'dock' and self.locked['tool_shed'] == True:
                print('\n''The tool shed door is locked tight, and without the key, you can\'t get inside. You realize you\'ll need to find the key or another way to get the tools you need.')
            elif direction == 'east' and self.current_location == 'dock' and self.locked['tool_shed'] == False:
                self.current_location = 'tool_shed'

    #Move commands in Tool Shed   
            elif direction == 'west' and self.current_location == 'tool_shed':
                self.current_location = 'dock'       

            else:
                print("Invalid command or you can\'t go that way.")




    #Check Ending function
    def check_ending(self):
        if all(value for value in self.clues.values()):
            print('\n''You have gathered all the clues scattered across the island. The pieces of the puzzle begin to fit together, and a sense of foreboding fills you as you make your way to a central location: the chapel, where your journey began to intertwine with your forgotten past.')
            self.endings['true'] = True
            self.endings['good'] = False
            self.clues['cell'] = False
    

    #Endings
    def end_game(self, ending):
        if ending == 'true':
            print('\n'"You step into the [boat], feeling the gentle sway beneath your feet. The engine starts with a sputter, then hums steadily. You take one last look at the island—the overgrown prison, the eerie chapel, and the dense forest. With a deep breath, you steer the boat away from the dock, leaving the island behind.") 
            print('\n''The boat glides through the water, the island slowly receding into the distance. You feel a mix of relief and unease. You\'ve escaped the immediate danger, but questions linger in your mind. You\'ve uncovered the truth about your past, but the memories of your actions weigh heavily on you.')
            print('\n''As the sun begins to rise, the island becomes a small dot on the horizon. The calm sea and the warmth of the morning sun offer a stark contrast to the cold, dark memories of the island. You focus on the future, knowing that you must find a way to live with your past and seek redemption.')
            print('\n''True Ending!')
            print('\n''You have escaped the island, carrying the heavy burden of your actions. The memories will haunt you, but the future offers a chance for redemption. Sometimes, survival means facing the truth and seeking a way to make amends.')
        elif ending == 'good':
            print('\n'"You step into the [boat], feeling the gentle sway beneath your feet. The engine starts with a sputter, then hums steadily. You take one last look at the island—the overgrown prison, the eerie chapel, and the dense forest. With a deep breath, you steer the boat away from the dock, leaving the island behind.") 
            print('\n''The boat glides through the water, the island slowly receding into the distance. You feel a mix of relief and unease. You\'ve escaped the immediate danger, but questions linger in your mind. What really happened in the prison? What role did you play in the horrors that unfolded there?')
            print('\n''As the sun begins to rise, the island becomes a small dot on the horizon. The calm sea and the warmth of the morning sun offer a stark contrast to the cold, dark memories of the island. You focus on the future, pushing thoughts of the past aside. Whatever the truth may be, you have a second chance now—a chance to start over, free from the shadows of the island.')
            print('\n''Good Ending!')
            print('\n''You have escaped the island, leaving its dark secrets behind. The memories may haunt you, but the future is yours to shape. Sometimes, survival means leaving the past where it belongs—in the shadows.')
        elif ending == 'bad' and self.current_location == 'lab':
            print('\n''You uncork the bottle and take a cautious sniff. Almost immediately, you feel dizzy and nauseous. The room spins, and you collapse to the floor. The substance is toxic, and you\'ve succumbed to its effects.')
            print('\n''The last thing you hear is the distant echo of your own heartbeat slowing down, then silence.')
            print('\n''Bad Ending!')
        elif ending == 'bad' and self.current_location == 'forest':
            print('\n''You attempt to climb down carefully. Fear grips you, causing you to slip and hit your head on a rock. The impact is fatal, and your journey on the island comes to a sudden and tragic end.')
            print('\n''The last thing you hear is the distant echo of your own heartbeat slowing down, then silence.')
            print('\n''Bad Ending!')
        elif ending == 'bad' and self.current_location == 'dock':
            print('\n''You decide to risk it and take the boat out to sea without making any repairs. As you head into the rough waters, the boat quickly begins to take on water and the engine sputters and dies. You are unable to control the vessel as it is battered by the waves and jagged rocks. The boat capsizes, and you drown in the cold, dark sea. Your journey ends here.')
            print('\n''The last thing you hear is the distant echo of your own heartbeat slowing down, then silence.')
            print('\n''Bad Ending!')
        elif ending == 'atonement' and self.current_location == 'dock'and self.endings['true'] == True and self.truth == True:
            print('\n''You step away from the [boat], your decision made. You walk back along the dock, each step feeling heavier than the last. You make your way back through the forest, past the chapel, and towards the laboratory where it all began.')
            print('\n''The island is eerily quiet as you make your way to the center of your past sins. You stand in the laboratory, the equipment broken and the smell of chemicals lingering in the air. You sit down at one of the old desks, pulling out a journal and a pen. You start to write, documenting everything: your experiments, the suffering you caused, and the truth you discovered.')
            print('\n''As you write, a sense of purpose fills you. You will stay on the island, facing the consequences of your actions and ensuring that the truth is known. The island becomes your penance, a place where you will spend the rest of your days atoning for your sins.')
            print('\n''Atonement Ending')
            print('\n''You have chosen to stay on the island, facing the consequences of your actions. The memories of your sins will haunt you, but you have taken the first step towards redemption. Sometimes, seeking forgiveness means facing the past and ensuring the truth is never forgotten.')
        self.game_over = True



#Start Game
if __name__ == "__main__":
    game = Game()
    game.start()