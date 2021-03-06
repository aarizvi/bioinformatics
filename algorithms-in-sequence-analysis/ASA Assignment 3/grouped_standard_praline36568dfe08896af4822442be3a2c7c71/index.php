<?php
$valuetable=$_POST['scoretable'];
$colorscheme=$_POST['color'];
$title='PRALINE sequence alignment results for job praline_grouped';
$pagetitle='PRALINE sequence alignment results';
include($_SERVER['DOCUMENT_ROOT'].'/includes/header.php');

echo "<blockquote><table>
<tr><td align=left valign=top><font face='Arial, Helvetica, Sans-serif' size=2 ><a href='http://www.ibi.vu.nl/programs/pralinewww/'><b>Back to PRALINE main page</b></a></td></tr>
<tr><td bgcolor=#003366><font face='Arial, Helvetica, Sans-serif' size=2>&nbsp;</td></tr>
<tr><td><font face='Arial, Helvetica, Sans-serif'><font face='Arial, Helvetica, Sans-serif' size=2>The PRALINE alignment process was completed in 11.0 seconds.<br><br>
Alignment score = 1683894.00<br>Alignment score per aligned residue pair = 16.84<br>Sequence identities = 79943<br>Percent sequence identity = 0.80<br>Number of sequences = 22<br>Alignment length = 530<br>Number of residues = 10109<br>Number of gaps = 1551<br>
<br><br></td></tr>
</table>
<table width=85% border=0 bordercolor='#0066CC' cellpadding=3 cellspacing=1><tr><td>
<form><input type='button' value='Save all data for this job (tar and gzipped file)' onClick=parent.location='results.tgz'></form><br>
<font face='Arial, Helvetica, Sans-serif' size=2><a href='alignment.fasta_ali'><b>Download the final alignment [alignment.fasta_ali]</b></a><br>
<a href='results.out'><b>Download PRALINE raw output file [results.out]</b></a><br>
<a href='sspredfiles0.php'><b>Download Secondary structure prediction files</b></a><br>
<br>&nbsp;</td></tr>
</table>
<table border=0 cellpadding=1 cellspacing=0>
";
switch ($colorscheme){
case "Hydrophobicity":
readfile("hydrophobicity0.html");
break;

case "Sec.Structure":
readfile("sstructure0.html");
break;

case "Conservation":
readfile("conservation0.html");
break;

case "Residue Type":
readfile("residues0.html");
break;

default:
readfile("conservation0.html");
break;
}
echo "</table>";
echo "</blockquote>";
include($_SERVER['DOCUMENT_ROOT'].'/includes/footer.php');

?>