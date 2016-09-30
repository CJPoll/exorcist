import pygame

''' Event handling and global even queue

	API
		events.Event
			User defined events should conform to this structure.  User defined
			events that need more data than just the event type can handle this
			in whatever way makes sense (ideally one or more instance
			variables).  User-defined events don't necessarily need to inherit,
			but the type instance variable is mandatory.
			
			See http://www.pygame.org/docs/ref/event.html#pygame.event.Event
			for Pygame event types.  User defined event types should probably
			be defined in the modules that produce the events.  Modules that
			consume events should import the modules that create events
			relevant to the consumer modules.
		
		events.queue
			This is the global event queue.  It should be treated as read only.
			Users should traverse this looking for events of types they are
			interested in.  Users should _never_ modify events.queue directly,
			nor should they modify events that are in the queue.
			
			The global event queue will be cleared and populated with new
			events each update.  If there is some reason an event needs to be
			carried to the next game loop, it should be pushed using
			events.push.
			
			(Yes, we could create a Queue class that would enforce the
			readonly-ness.  We could embed events.push() into the object.  We
			could even make traversal of Queue objects return copies of events,
			to prevent modification.  Instead, we will use Python's motto with
			regards to private variables, "We are all consenting adults here."
			Follow the API rules listed here, and we can use this far more
			efficient code without any problems.)

		events.update
			This should be called every game loop.  It will clear the event
			queue and populate it with new events, including pushed
			user-defined events, and events on Pygame's event queue.
			
		events.push
			This should be used to add user-defined events to the global event
			queue.  It takes 1 argument, which must conform to events.Event.
'''


# This  will be the global even queue
queue = []

# This will keep events that need to be added
# to the queue for the next game loop
_buffer = []


def update():
	''' Update the event queue
	
		This should be run each game loop.
		
		Manages the global event queue by overwriting the buffer
		to the queue and then pushing all events from the Pygame
		event queue.
	'''
	queue = _buffer						# Makes queue point to the buffer list
	queue.extend(pygame.event.get())	# Add all events from Pygame's queue
	_buffer = []						# Create new buffer for next loop

	
def push(event):
	'''Push new user-defined events onto the buffer
	
		event - Must conform to Event type (ie., must have "type"
		instance variable)
	'''
	_buffer.append(event)


class Event(object):
	'''User defined events should conform to this structure
	
		User defined events that need more data than just the event type can be
		handled as needed, so long as the "type" instance variable exists.
		
		It is not necessary to inherit from this.  User defined events can be
		instances of this class, and additional data can be added after an
		event is created (this is how Pygame seems to handle its event
		objects).
	'''
	
	def __init__(self, type):
		self.type = type