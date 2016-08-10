import csv
import sys

def opencsv(filename):
	csvfile = open(filename, "rU")
	csvfile.seek(0)
	reader = csv.reader(csvfile, dialect = "excel")

	
#	for row in reader:
#		for i, x in enumerate(row):
#			if len(x)< 1:
#				x = row[i] = 0
 #   	reader.writerow(','.join(str(x) for x in row)
	
	y = []
	Glass = []
	cpx = []
	fspar = []
	qtz = []
	amph = []
	olivine = []
	mag = []
	ilm = []
	chev = []
	ap = []
	fl = []
	po = []
	firstline = True
	
	for line in reader:
		if firstline:
			firstline = False
			continue
			
		y.append(float(line[1]))
		Glass.append(float(line[2]))
		cpx.append(float(line[3]))
		fspar.append(float(line[4]))
		qtz.append(float(line[5]))
		amph.append(float(line[6]))
		olivine.append(float(line[7]))
		mag.append(float(line[8]))
		ilm.append(float(line[9]))
		chev.append(float(line[10]))
		ap.append(float(line[11]))
		fl.append(float(line[12]))
		po.append(float(line[13]))
		
	def all_zeroes(items):
		return all(x == 0 for x in items)
	
	x_vals = []
	if all_zeroes(Glass) is False:
		x_vals.append(Glass)
	if all_zeroes(cpx) is False:
		x_vals.append(cpx)
	if all_zeroes(fspar) is False:
		x_vals.append(fspar)
	if all_zeroes(qtz) is False:
		x_vals.append(qtz)
	if all_zeroes(amph) is False:
		x_vals.append(amph)
	if all_zeroes(olivine) is False:
		x_vals.append(olivine)
	if all_zeroes(mag) is False:
		x_vals.append(mag)
	if all_zeroes(ilm) is False:
		x_vals.append(ilm)
	if all_zeroes(chev) is False:
		x_vals.append(chev)
	if all_zeroes(ap) is False:
		x_vals.append(ap)
	if all_zeroes(fl) is False:
		x_vals.append(fl)
	if all_zeroes(po) is False:
		x_vals.append(po)
	
	return(y, x_vals, Glass, cpx, fspar, qtz, amph, olivine, mag, ilm, chev, ap, fl, po)
