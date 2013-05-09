<?php
	include('../model/coBdd.php');
	$request = $bdd->query("SELECT id_msg as id, title, msg, date_msg
                           FROM msg
                           ORDER BY id_msg DESC");
    $i = 0;
    echo '<div>';
    while ($msg = $request->fetch())
    {

                if ($i == 0)
                {
                    echo '<div class="container-fluid"><div class="row-fluid">';
                }
?>
                         <div id="<?php echo $msg['id']; ?>" class="span3 artc">
                            <div class="hero-unit">
                                <h2><?php echo $msg['title']?></h2>
                                <p>
                                    <?php //echo $msg['msg']; ?>
                                </p>
                                <p>
                                    <?php echo $msg['date_msg']; ?>
                                </p>
                            </div>
                        </div>
                <?php
                if ($i == 3)
                {
                    echo '</div></div>';
                    $i = 0;
                }
                else
                    $i++;
    }
    echo '</div>';
?>
