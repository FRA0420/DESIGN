from typing import Self

# Specialised domain 18..31
# - immutable

class Voto:
	# campi dati:
	# _value:int

	def __init__(self, v:int):
		if v < 18 or v > 31:
			raise ValueError(f"Value v must be between 18 and 31, now {v}")
		self._value = v

	def valore(self)->int:
		return self._value

	def __hash__(self)->int:
		return hash(self.valore())
	
	def __eq__(self, other)->bool:
		if other is None:
			return False

		if not isinstance(other, type(self)):
			# try to cast other to type(self) using available __init__():
			try:
				other = type(self)(other)
			except:
				return False

		assert type(other) == type(self)
		
		if hash(self) != hash(other):
			return False
		else:
			return self.valore() == other.valore()


	def __lt__(self, other)->bool:
		if not isinstance(other, type(self)):
			try:
				other = type(self)(other)
			except:
				raise TypeError(f"Operator < not defined between Voto and {type(other)}")
		return self.valore() < other.valore()

	def __gt__(self, other):
		if not isinstance(other, type(self)):
			try:
				other = type(self)(other)
			except:
				raise TypeError(f"Operator < not defined between Voto and {type(other)}")
		return self.valore() > other.valore()


	def __repr__(self)->str:
		return repr(self.valore())

	# useless, just for testing
	def __add__(self, other)->Self:
		ov:int = other.valore() if isinstance(other, type(self)) else other
		return type(self)(self.valore() + ov)

	# useless, just for testing
	def __sub__(self, other)->Self:
		ov:int = other.valore() if isinstance(other, type(self)) else other
		return type(self)(self.valore() - ov)