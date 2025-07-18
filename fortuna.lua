math.randomseed(os.time())

--implementando orientação a objetos em Lua
board = {}
board.__index = board

--método para a contrução de novas mesas
function board:create()
	local object = {} --nova instância do objeto
	setmetatable(object, self) -- board como metatabela de object

	object.coins = { nil, nil, nil, nil, nil }
	return object
end

function board:show()
	print(table.concat(self.coins, "  "))
end

-- Criar o board:dice que gera sequencialmente o ante-flop, flop, turn
-- e river
function board:dice()
	if self.coins[1] == nil or self.coins[2] == nil then
		self.coins[1] = self.coins[1] or math.random(2)
		self.coins[2] = self.coins[2] or math.random(2)
		return
	end

	if self.coins[3] == nil then
		self.coins[3] = math.random(2)
		return
	end

	if self.coins[4] == nil then
		self.coins[4] = math.random(2)
		return
	end

	if self.coins[5] == nil then
		self.coins[5] = math.random(2)
		return
	end
end

player = {}
player.__index = player

function player:create(name, cash)
	local object = {}
	setmetatable(object, self)

	object.coins = { nil, nil, nil, nil, nil }
	object.name = name or nil
	object.cash = cash or 1000
	return object
end

function player:hand(hand)
	self.coins = hand
end

mesa = board:create()
for i = 1, 4 do
	mesa:dice()
	mesa:show()
end
