md input
md output
for /L %%D in (0,1,9) do move data.i%%D input\input0%%D.txt
for /L %%D in (0,1,9) do move data.o%%D output\output0%%D.txt
for /L %%D in (10,1,20) do move data.i%%D input\input%%D.txt
for /L %%D in (10,1,20) do move data.o%%D output\output%%D.txt
zip -r test.zip *put
rd input /S /Q
rd output /S /Q