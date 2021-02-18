import os
import argparse
import sys

normal_color = "\33[00m"
info_color = "\033[1;33m"
red_color = "\033[1;31m"
green_color = "\033[1;32m"
whiteB_color = "\033[1;37m"
detect_color = "\033[1;34m"
banner_color="\033[1;33;40m"
end_banner_color="\33[00m"


######### Check Arguments
def checkArgs():

        print (banner_color + "##     ##    ###     ######   ####  ######  ##      ##  #######  ########  ########   ###### ")
        print (banner_color + "###   ###   ## ##   ##    ##   ##  ##    ## ##  ##  ## ##     ## ##     ## ##     ## ##    ##")
        print (banner_color + "#### ####  ##   ##  ##         ##  ##       ##  ##  ## ##     ## ##     ## ##     ## ##      ")
        print (banner_color + "## ### ## ##     ## ##   ####  ##  ##       ##  ##  ## ##     ## ########  ##     ##  ###### ")
        print (banner_color + "##     ## ######### ##    ##   ##  ##       ##  ##  ## ##     ## ##   ##   ##     ##       ##")
        print (banner_color + "##     ## ##     ## ##    ##   ##  ##    ## ##  ##  ## ##     ## ##    ##  ##     ## ##    ##")
        print (banner_color + "##     ## ##     ##  ######   ####  ######   ###  ###   #######  ##     ## ########   ###### ")
        print (banner_color + "                                                                                             ")
        print (banner_color + "                                                                     by @magichk             ")


        parser = argparse.ArgumentParser()
        parser = argparse.ArgumentParser(description=red_color + 'MagicWords 1.0\n' + info_color)
        parser.add_argument('-f', "--file", action="store",
                                                dest='file',
                            help="Name of the file resultant with the dict")
        parser.add_argument('-w', "--word", action="store",
                                                dest='word',
                            help="Word to use to create a new dict")
        parser.add_argument('-y', "--years", action="store_true",
                                                dest='years',
                            help="Add years from 2000 to 2021 at the final of your string")
        parser.add_argument('-r', "--replace", action="store_true",
                                                dest='replace',
                            help="Replace vowels with numbers")
        parser.add_argument('-g', "--generic", action="store_true",
						dest='generic',
                            help="Generic words like months of the year")
        args = parser.parse_args()

        return args

#Años
def tiempo(word, filename):
	print(green_color + "[" + red_color+ "+" + green_color +"] " + whiteB_color + "Generating dict with years...")
	fichero = open(filename, "w")
	cont = 0
	while (cont <= 21):
		if (cont <= 9):
		    fichero.write(word+"0"+str(cont)+"\n")
		    fichero.write(word+"0"+str(cont)+"!"+"\n")
		    fichero.write(word+"0"+str(cont)+"#"+"\n")
		else:
		    fichero.write(word+str(cont)+"\n")
		    fichero.write(word+str(cont)+"!"+"\n")
		    fichero.write(word+str(cont)+"#"+"\n")
		cont = cont + 1




	ano = 2000
	flag = 0

	inicio = word.find("20", len(word)-5)
	while (ano <= 2021):
		if (inicio == -1):
			newword = word + str(ano)
			#print (newword)
			fichero.write(newword+"\n")
			fichero.write(newword+"!\n")
			fichero.write(newword+"#\n")
			newword = word.capitalize()
			#print (newword + str(ano))
			fichero.write(newword+str(ano)+"\n")
			fichero.write(newword+str(ano)+"!\n")
			fichero.write(newword+str(ano)+"#\n")

		elif (flag == 0):
			fichero.write(word+"!\n")
			fichero.write(word+"#\n")
			flag = 1
		ano = ano + 1



	fichero.close()


#vocales a numeros con crunch
def chartoint(word, printornot, filename):
	if (printornot == 0):
		print(green_color + "[" + red_color+ "+" + green_color +"] " + whiteB_color + "Generating dict replacing vowels by numbers with crunch...")
	else:
		print(green_color + "[" + red_color+ "+" + green_color +"] " + whiteB_color + "Generating dict with @ and replacing vowels by numbers with crunch...")
	total = 0
	newword = ""
	#how many vowels has the word?
	for letter in word:
		if (letter == "a" or letter == "A" or letter == "e" or letter == "E" or letter == "i" or letter == "I" or letter == "o" or letter == "O" or letter == "u" or letter == "U"):
			letter = "%"

		newword = newword + letter
		total = total + 1

	#print(newword)
	#use crunch to generate a dict.
	os.system("crunch "+str(total)+" "+str(total)+" @ -t \""+newword+"\" -o crunch.txt > /dev/null 2>&1")
	openfile = open("crunch.txt", "r")
	myfile = openfile.readlines()
	fichero = open(filename, "a")
	for line in myfile:
		line = line[0:len(line)-1]
		fichero.write(line+"\n")
		fichero.write(line+"!\n")
		fichero.write(line+"#\n")
	fichero.close()
	os.system("rm -rf crunch.txt")

#Substituir A/a por @
def arroba(word, filename):
	print(green_color + "[" + red_color+ "+" + green_color +"] " + whiteB_color + "creating character @ if it's necessary...")
	fichero = open(filename, "a")
	flag = 0
	for letter in word:
		if (letter == "a"):
			flag = 1
		elif (letter == "A"):
			flag = 2
	if (flag >= 1):
		wordnew = word.replace("a", "@")
		fichero.write(wordnew+"\n")
		fichero.write(wordnew+"!\n")
		fichero.write(wordnew+"#\n")
	if (flag == 2):
		wordnew = word.replace("A", "@")
		fichero.write(wordnew+"\n")
		fichero.write(wordnew+"!\n")
		fichero.write(wordnew+"#\n")
		fichero.close()
		chartoint(wordnew,1, filename)
	fichero.close()
def generico(filename):
	fichero = open(filename, "a")
	elementos = [ "enero", "january", "febrero", "february", "marzo", "march", "abril", "april", "junio", "june", "julio", "july", "agosto", "august", "septiembre", "september", "octubre", "october", "noviembre", "november", "diciembre", "december", "primavera", "spring", "verano", "summer", "otoño", "autumn", "invierno", "winter" ]

	cont = 0
	for item in elementos:
		ano = 2005
		while (ano <= 2021):
			fichero.write(elementos[cont]+str(ano)+"\n")
			fichero.write(elementos[cont]+str(ano)+"!\n")
			fichero.write(elementos[cont]+str(ano)+"#\n")
			fichero.write(elementos[cont].capitalize()+str(ano)+"\n")
			fichero.write(elementos[cont].capitalize()+str(ano)+"\n")
			fichero.write(elementos[cont].capitalize()+str(ano)+"\n")
			ano = ano + 1
		cont = cont + 1
	fichero.close()




#Main
if __name__ == "__main__":
        args = checkArgs()

        if (args.file):
                if (args.word):
                        word = args.word

                if (args.file):
                        filename = args.file
                        inicio = filename.find(".txt")
                        if (inicio == -1):
                                filename = filename+".txt"
                else:
                        filename = "dict.txt"

                if (args.years):
                        if (args.word):
                                tiempo(word, filename)
                if (args.replace):
                        if (args.word):
                                chartoint(word,0, filename)
                if (args.generic):
                        generico(filename)
                if (args.word):
                        arroba(word, filename)

                print(green_color + "[" + red_color+ "+" + green_color +"] " + banner_color + "Dictionary was saved in " + green_color + filename  + banner_color + " file!")

        else:
                print (red_color + "[-] Please use -w option to introduce a word to make a dict")
