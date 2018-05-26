<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
	<title>АИС</title>
	<style>
		table{
			border: 2px solid black;
			padding: 0;
		}
		thead td{
			margin: 0;
			border-bottom: 2px solid black;
			border-right: 2px solid black;
		}
		tbody tr{
			border: 1px solid black;
		}
	</style>
</head>
<body>
<table>
	<thead><tr>
		<td>№<br>п/п</td>
		<td>Наименование</td>
		<td>Единица<br>измерения</td>
		<td>Количество</td>
		<td>Цена</td>
		<td>Сумма</td>
	</tr></thead>
	<tbody>
		<?php
			for ($i=0; $i<10; $i++)
				echo '<tr style="border: 1px solid black;">
						<td>привет</td>
						<td></td>
						<td></td>
						<td></td>
						<td></td>
						<td></td>
					</tr>';
		?>
	</tbody>
</table>
</body>
</html>