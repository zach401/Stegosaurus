from PIL import Image
import hashlib

def encode(in_image, out_image, message, pwd):
	im = Image.open(in_image)
	width, height = im.size
	total_size = width*height*3

	bits = __str_to_bits(message + chr(3))
	if len(bits) > total_size:
		raise Exception('ERROR: Image is not large enough to store data. This image can only store {0} bytes.'.format(total_size/8))

	bit_num = 0
	used_locs = set()
	for bit in bits:
		bit_loc = __bit_num_to_loc(bit_num, total_size, pwd)
		while bit_loc in used_locs:
			bit_loc += 1
			if bit_loc >= total_size:
				bit_loc = 0
		used_locs.add(bit_loc)
		__put_bit(im, bit, bit_loc)
		bit_num += 1
	im.save(out_image)


def decode(im_file, pwd):
	received = Image.open(im_file)
	width, height = received.size
	total_size = width * height * 3
	decoded = []

	bit_num = 0
	used_locs = set()
	next_char = 0
	bits_in_char = 0
	while True:
		bit_loc = __bit_num_to_loc(bit_num, total_size, pwd)
		while bit_loc in used_locs:
			bit_loc += 1
			if bit_loc >= total_size:
				bit_loc = 0
		used_locs.add(bit_loc)

		bit = __get_bit(received, bit_loc)
		bit_num += 1

		next_char |= bit << bits_in_char
		bits_in_char += 1
		if bits_in_char == 8:
			if next_char == 3:
				break
			else:
				decoded.append(chr(next_char))
				bits_in_char = 0
				next_char = 0
	return ''.join(decoded)


def __str_to_bits(message):
	m = message.encode('utf-8')
	bits = []
	for char in m:
		for i in range(8):
			bit = 1 if (char >> i) & 1 else 0
			bits.append(bit)
	return bits

def __bit_num_to_loc(bit_num, size, pwd):
	hash1 = int(hashlib.sha224(pwd.encode('utf-8')).hexdigest(), 16)
	bit_loc = (hash1*bit_num**2 + hash1//2*bit_num + bit_num) % size
	return bit_loc
	return bit_num

def __get_bit(im, bit_loc):
	width, height = im.size
	pix_num = bit_loc // 3
	pix_x = pix_num % width
	pix_y = pix_num // width
	if pix_y >= height:
		raise(Exception('INVALID INPUT FILE'))
	color = bit_loc % 3
	pix = im.getpixel((pix_x, pix_y))
	return pix[color] & 1


def __put_bit(im, bit, bit_loc):
	width, height = im.size
	pix_num = bit_loc // 3
	pix_x = pix_num % width
	pix_y = pix_num // width
	if pix_y >= height:
		raise (Exception('IMAGE IS TOO SMALL TO STORE DATA'))
	color = bit_loc % 3
	org_pix = list(im.getpixel((pix_x, pix_y)))
	org_pix[color] =  org_pix[color] & (~0 << 1) | bit
	im.putpixel((pix_x, pix_y), tuple(org_pix))