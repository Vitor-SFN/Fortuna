math.randomseed(os.time())

-- Criar a classe game que deve conter board, Players e pot como características
-- Criar a classe pot e métodos check, bet, raise para Player

--implementando orientação a objetos em Lua
Board = { coins = { nil, nil, nil, nil, nil } }

--método para a contrução de novas mesas
function Board:new(o)
	o = o or {} --nova instância do objeto
	setmetatable(o, self) -- Board como metatabela de object
	self.__index = self
	return o
end

function Board:show()
	print(table.concat(self.coins, "  "))
end

function Board:flipCoin()
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

Player = { name = nil, cash = 1000, coins = { nil, nil, nil, nil, nil } }

function Player:new(o)
	o = o or {}
	setmetatable(o, self)
	self.__index = self
	return o
end

function Player:showHand()
	print(table.concat(self.coins, "  "))
end

mesa = Board:new()
for _ = 1, 4 do
	mesa:flipCoin()
	mesa:show()
end

Players = {}
Number_Players = 0

print("Bem-vindos a Fortuna!\n")

while true do
	io.write("\nQual o nome do jogador que deseja jogar?\n")
	local alias = io.read()
	if alias == "" then
		break
	end
	Number_Players = Number_Players + 1

	io.write("Qual a mão de " .. alias .. "?\n")
	local hand = io.read()
	io.write("\27[1A") -- Move o cursor uma linha para cima (para a linha da pergunta)
	io.write("\27[2K") -- Apaga a linha inteira

	local coins_table = {}

	for num_str in string.gmatch(hand, "%S+") do -- %S+ significa "um ou mais caracteres não-espaço"
		local number = tonumber(num_str)
		if #coins_table >= 5 then
			break
		end
		if number ~= nil and (number == 1 or number == 2) then -- verificando validade
			table.insert(coins_table, number)
		else
			print("Aviso: '" .. num_str .. "' não é um número válido e foi ignorado.")
		end
	end

	-- Se o jogador não escolher uma mão completa, o restante é escolhido de modo aleatório
	for i = #coins_table + 1, 5 do
		coins_table[i] = math.random(2)
	end

	Players[Number_Players] = Player:new({ name = alias, coins = coins_table })
	--Players[Number_Players]:showHand()
end

-- criar uma tabela de estados: pré-flop, flop, river, etc
-- incluir dentro de um while dos turnos
if Number_Players <= 1 then
	print("Não há jogadores suficientes")
end
