#!/bin/bash
#exec 3>&1 4>&2
#trap 'exec 2>&4 1>&3' 0 1 2 3
#exec 1>log.txt 2>&1

# export CC=gcc
# export CXX=g++

export src=$PWD/../
export markdown=markdown
export rstudio=generate
export rstudio_img=../plots
export output=pdf
export out_image=$src/$output/img
# export reconfigure=false
export clean=false
# export wipe=false
# export cplus=true
export rlang=true

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine="Linux";;
    Darwin*)    machine="Mac";;
    CYGWIN*)    machine="Cygwin";;
    MINGW*)     machine="MinGw";;
	MSYS*)      machine="MSYS_NT-10.0";;
    *)          machine="UNKNOWN:${unameOut}"
esac

echo "Current OS: ${machine} with uname: ${unameOut}..."
if [ "$machine" = "Mac" ] || [ "$machine" = "Cygwin" ]; then
	echo "Mac, Cygwin are currently unsupported."
fi

cd $src

# if [[ ! -e $build ]]; then
#     mkdir $build
# elif [[ ! -d $build ]]; then
#     echo "$build already exists but is not a directory" 1>&2
# fi

# if [[ ! -e $output ]]; then
#     mkdir $output
# elif [[ ! -d $output ]]; then
#     echo "$output already exists but is not a directory" 1>&2
# fi


# if [[ ! -e $out_image ]]; then
#     mkdir $out_image
# elif [[ ! -d $out_image ]]; then
#     echo "$out_image already exists but is not a directory" 1>&2
# fi


# while getopts b:o:rnmcw flag
while getopts cw flag
do
    case "${flag}" in
    # b) 
	# 	echo "received -build with $OPTARG"
	# 	build=${OPTARG}
	# 	;;
    # o) 
	# 	echo "received -output with $OPTARG"
	# 	output=${OPTARG}
	# 	;;
	# r)
	# 	echo "received -reconfigure: cmake src"
	# 	export reconfigure=true
	# 	;;
	# n)
	# 	echo "received -no_cplusplus: only running R"
	# 	export cplus=false
	# 	;;
	# m)
	# 	echo "received -no_rlang: only running cplusplus"
	# 	export rlang=false
	# 	;;
	c) 
		echo "received -clean: cleaning all output"
		export clean=true
		;;
	w) 	
		echo "received -wipe: cleaning all output (not generating PDF)"
		export clean=true
		export rlang=false
		;;
    esac
done

echo "Source (Absolute) Directory: $src"
echo "Markdown (Relative) Directory : $markdown"
echo "Plots (Relative) Directory : $rstudio_img"
echo "Output (Relative) Directory: $output"

# if [ "$clean" = true ] ; then
# 	cd $src$build
# 	make clean
# 	echo "Swept and dusted..."
# 	exit
# fi

if [ "$clean" = true ] ; then
	cd $output
	rm -r *
	echo "Wiped output."
	exit
fi

cd $src;

# if [ "$reconfigure" = true ] ; then
# 	echo "CMAKE Configure ...";
# 	if [ "$machine" = "MinGw" ] ; then
# 		cmake -G "MSYS Makefiles" $rsrc
# 	elif [ "$machine" = "Linux" ] ; then
# 		cmake $rsrc
# 	else
# 		cmake $rsrc
# 	fi
# 	#echo "CMAKE Configure ..."; cmake $rsrc;
# fi

# if [ "$cplus" = true ] ; then
# 	echo "make ..."; make -j8
# 	echo "run Tests"; ./Tests
# fi

export rstudio_out_img=../$output/img

if [ "$rlang" = true ] ; then
	echo 'Generating R Markdown ....'
	cd $src$rstudio/base
	if [ "$machine" = "MinGw" ] || [ "$machine" = "Cygwin" ] || [ "$machine" = "MSYS" ]; then
 		py replace.py
 	elif [ "$machine" = "Linux" ] ; then
 		python3 replace.py
	else
 		python3 replace.py
	fi
	echo 'Generating PDF ....'
	cd $src$rstudio
	Rscript -e 'pagedown::chrome_print('"'article.rmd'"')' > log_r.txt

	make4ht article.tex styling/template.tex --config styling/mk4ht
	texify.exe --pdf --synctex=1 --clean article.tex
	files="$(ls -I.git -I*.txt -I*.html -I*.css -I*.pdf -I*.json -I*.gif -I*.jpg -I*.png -I*.sh -Iio*.* -Ipackages.bib -p | grep -v /)"
	rm $files

	cat styling/def.css >> article.css

	cd $src
	mv $rstudio/article.html $output/article.html
	cp $rstudio/styling/*.jpg $output/
	mv $rstudio/*.png $output/
	mkdir $output/article_files/
	cp -r $rstudio/article_files/ $output/article_files/
	mv $rstudio/article.css $output/article.css
	mv $rstudio/article.pdf $output/article.pdf
fi