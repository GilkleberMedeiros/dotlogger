from dotlogger import *


class TestSettings:
    set_classifier_1 = "set1"
    set_classifier_2 = "set2"
    class_classifier_1 = "class1"
    class_classifier_2 = "class2"
    id_classifier_1 = "id1"
    id_classifier_2 = "id2"
    log_path = "./abc/def/ghi.txt"

    def test_block_deblock_all(self) -> None:
        """
        Testa se a configuração de bloquear todos os logs 
        está funcionando corretamente. Usando as funções
        get_all_logs_blocked e block_all_logs.
        """
        assert get_all_logs_blocked() == False
        block_all_logs()
        assert get_all_logs_blocked() == True
        block_all_logs(block=False)
        assert get_all_logs_blocked() == False

    def test_block_deblock_set_1(self) -> None:
        """
        Testa se os logs estão sendo bloqueados através
        do classifier SET, passando um SET de 
        cada vez para ser bloqueado e então removendo o 
        bloqueio de todos de uma vez.
        """
        assert get_log_blocked_by_classifier(
            self.set_classifier_1, "set"
        ) == False
        assert get_log_blocked_by_classifier(
            self.set_classifier_2, "set"
        ) == False

        block_log_by_classifier(
            self.set_classifier_1, "set"
        )

        assert get_log_blocked_by_classifier(
            self.set_classifier_1, "set"
        ) == True
        assert get_log_blocked_by_classifier(
            self.set_classifier_2, "set"
        ) == False

        block_log_by_classifier(
            self.set_classifier_2, "set"
        )
        
        assert get_log_blocked_by_classifier(
            self.set_classifier_1, "set"
        ) == True
        assert get_log_blocked_by_classifier(
            self.set_classifier_2, "set"
        ) == True

        remove_log_blocked_by_classifier(
            self.set_classifier_1, "set"
        )
        remove_log_blocked_by_classifier(
            self.set_classifier_2, "set"
        )

        assert get_log_blocked_by_classifier(
            self.set_classifier_1, "set"
        ) == False
        assert get_log_blocked_by_classifier(
            self.set_classifier_2, "set"
        ) == False

    def test_block_deblock_class_1(self) -> None:
        """
        Testa se os logs estão sendo bloqueados através
        do classifier CLASS, passando uma CLASS de 
        cada vez para ser bloqueado e então removendo o 
        bloqueio de todos de uma vez.
        """
        assert get_log_blocked_by_classifier(
            self.class_classifier_1, "class"
        ) == False
        assert get_log_blocked_by_classifier(
            self.class_classifier_2, "class"
        ) == False

        block_log_by_classifier(
            self.class_classifier_1, "class"
        )

        assert get_log_blocked_by_classifier(
            self.class_classifier_1, "class"
        ) == True
        assert get_log_blocked_by_classifier(
            self.class_classifier_2, "class"
        ) == False

        block_log_by_classifier(
            self.class_classifier_2, "class"
        )
        
        assert get_log_blocked_by_classifier(
            self.class_classifier_1, "class"
        ) == True
        assert get_log_blocked_by_classifier(
            self.class_classifier_2, "class"
        ) == True

        remove_log_blocked_by_classifier(
            self.class_classifier_1, "class"
        )
        remove_log_blocked_by_classifier(
            self.class_classifier_2, "class"
        )

        assert get_log_blocked_by_classifier(
            self.class_classifier_1, "class"
        ) == False
        assert get_log_blocked_by_classifier(
            self.class_classifier_2, "class"
        ) == False

    def test_block_deblock_id_1(self) -> None:
        """
        Testa se os logs estão sendo bloqueados através
        do classifier ID, passando um ID de 
        cada vez para ser bloqueado e então removendo o 
        bloqueio de todos de uma vez.
        """
        assert get_log_blocked_by_classifier(
            self.id_classifier_1, "id"
        ) == False
        assert get_log_blocked_by_classifier(
            self.id_classifier_2, "id"
        ) == False

        block_log_by_classifier(
            self.id_classifier_1, "id"
        )

        assert get_log_blocked_by_classifier(
            self.id_classifier_1, "id"
        ) == True
        assert get_log_blocked_by_classifier(
            self.id_classifier_2, "id"
        ) == False

        block_log_by_classifier(
            self.id_classifier_2, "id"
        )
        
        assert get_log_blocked_by_classifier(
            self.id_classifier_1, "id"
        ) == True
        assert get_log_blocked_by_classifier(
            self.id_classifier_2, "id"
        ) == True

        remove_log_blocked_by_classifier(
            self.id_classifier_1, "id"
        )
        remove_log_blocked_by_classifier(
            self.id_classifier_2, "id"
        )

        assert get_log_blocked_by_classifier(
            self.id_classifier_1, "id"
        ) == False
        assert get_log_blocked_by_classifier(
            self.id_classifier_2, "id"
        ) == False

    def test_write_all_logs_to(self) -> None:
        """
        Testa se a configuração que permite escrever 
        todos os logs para um mesmo lugar está funcionando.
        Usando as funções get_write_all_logs_to e 
        write_all_logs_to.
        """
        assert get_write_all_logs_to() == ""

        write_all_logs_to(self.log_path)

        assert get_write_all_logs_to() == self.log_path

        write_all_logs_to("")

        assert get_write_all_logs_to() == ""

    def test_write_log_to_by_classifier_set_1(self) -> None:
        """
        Testa se os logs estão sendo configurados 
        sobre onde eles serão escritos através
        do classifier SET, passando um SET de 
        cada vez para ser configurado e então removendo a 
        configuração de todos de uma vez.
        """
        assert get_write_log_to_by_classifier(
            self.set_classifier_1, "set"
        ) == ""
        assert get_write_log_to_by_classifier(
            self.set_classifier_2, "set"
        ) == ""

        write_log_to_by_classifier(
            self.set_classifier_1, self.log_path, "set"
        )

        assert get_write_log_to_by_classifier(
            self.set_classifier_1, "set"
        ) == self.log_path
        assert get_write_log_to_by_classifier(
            self.set_classifier_2, "set"
        ) == ""

        write_log_to_by_classifier(
            self.set_classifier_2, self.log_path, "set"
        )
        
        assert get_write_log_to_by_classifier(
            self.set_classifier_1, "set"
        ) == self.log_path
        assert get_write_log_to_by_classifier(
            self.set_classifier_2, "set"
        ) == self.log_path

        remove_write_log_to_by_classifier(
            self.set_classifier_1, "set"
        )
        remove_write_log_to_by_classifier(
            self.set_classifier_2, "set"
        )

        assert get_write_log_to_by_classifier(
            self.set_classifier_1, "set"
        ) == ""
        assert get_write_log_to_by_classifier(
            self.set_classifier_2, "set"
        ) == ""

    def test_write_log_to_by_classifier_class_1(self) -> None:
        """
        Testa se os logs estão sendo configurados 
        sobre onde eles serão escritos através
        do classifier CLASS, passando um CLASS de 
        cada vez para ser configurado e então removendo a 
        configuração de todos de uma vez.
        """
        assert get_write_log_to_by_classifier(
            self.class_classifier_1, "class"
        ) == ""
        assert get_write_log_to_by_classifier(
            self.class_classifier_2, "class"
        ) == ""

        write_log_to_by_classifier(
            self.class_classifier_1, self.log_path, "class"
        )

        assert get_write_log_to_by_classifier(
            self.class_classifier_1, "class"
        ) == self.log_path
        assert get_write_log_to_by_classifier(
            self.class_classifier_2, "class"
        ) == ""

        write_log_to_by_classifier(
            self.class_classifier_2, self.log_path, "class"
        )
        
        assert get_write_log_to_by_classifier(
            self.class_classifier_1, "class"
        ) == self.log_path
        assert get_write_log_to_by_classifier(
            self.class_classifier_2, "class"
        ) == self.log_path

        remove_write_log_to_by_classifier(
            self.class_classifier_1, "class"
        )
        remove_write_log_to_by_classifier(
            self.class_classifier_2, "class"
        )

        assert get_write_log_to_by_classifier(
            self.class_classifier_1, "class"
        ) == ""
        assert get_write_log_to_by_classifier(
            self.class_classifier_2, "class"
        ) == ""

    def test_write_log_to_by_classifier_id_1(self) -> None:
        """
        Testa se os logs estão sendo configurados 
        sobre onde eles serão escritos através
        do classifier ID, passando um ID de 
        cada vez para ser configurado e então removendo a 
        configuração de todos de uma vez.
        """
        assert get_write_log_to_by_classifier(
            self.id_classifier_1, "id"
        ) == ""
        assert get_write_log_to_by_classifier(
            self.id_classifier_2, "id"
        ) == ""

        write_log_to_by_classifier(
            self.id_classifier_1, self.log_path, "id"
        )

        assert get_write_log_to_by_classifier(
            self.id_classifier_1, "id"
        ) == self.log_path
        assert get_write_log_to_by_classifier(
            self.id_classifier_2, "id"
        ) == ""

        write_log_to_by_classifier(
            self.id_classifier_2, self.log_path, "id"
        )
        
        assert get_write_log_to_by_classifier(
            self.id_classifier_1, "id"
        ) == self.log_path
        assert get_write_log_to_by_classifier(
            self.id_classifier_2, "id"
        ) == self.log_path

        remove_write_log_to_by_classifier(
            self.id_classifier_1, "id"
        )
        remove_write_log_to_by_classifier(
            self.id_classifier_2, "id"
        )

        assert get_write_log_to_by_classifier(
            self.id_classifier_1, "id"
        ) == ""
        assert get_write_log_to_by_classifier(
            self.id_classifier_2, "id"
        ) == ""

