<?php
chdir($_SERVER['DOCUMENT_ROOT']);
//echo json_encode($_SERVER);EXIT;

if (is_file($_SERVER['DOCUMENT_ROOT'].'/'.$_SERVER['SCRIPT_NAME'])) {
    return false;
}else{
	include __DIR__ . '/index.php';
}
