$(document).ready(function() {
    $('#add-income-button').click(function() {
        $('#additional-income-container').append(`
            <div class="additional-income-group">
              <div class="row">
                <div class="mb-3 col-md-2">
                   
                    <div class="input-group">
                        <input type="text" name="additional_income[]" class="form-control" id="additional_income_new" value="">
                        <span class="input-group-text">$</span>
                    </div>
                </div>
                <div class="mb-3 col-md-6">
                    
                    <input type="text" name="additional_income_description[]" class="form-control" id="additional_income_description_new" value="">
                </div>
                <div class="mb-3 col-md-2">
                    
                    <input type="date" name="additional_income_start[]" class="form-control" id="additional_income_start_new" value="">
                </div>
                <div class="mb-3 col-md-2">
                    
                    <input type="date" name="additional_income_end[]" class="form-control" id="additional_income_end_new" value="">
                </div>
                </div>
            </div>
        `);
    });

    $('#add-one-time-income-button').click(function() {
        $('#one-time-income-container').append(`
            <div class="one_time_income-group">
                <div class="row">
                <div class="mb-3 col-md-2">
                    
                    <div class="input-group">
                        <input type="text" name="one_time_income[]" class="form-control"  value="">
                        <span class="input-group-text">$</span>
                    </div>
                </div>
                <div class="mb-3 col-md-6">
                    
                    <input type="text" name="one_time_income_description[]" class="form-control"  value="">
                </div>
                <div class="mb-3 col-md-2">
                
                    <input type="date" name="one_time_income_start[]" class="form-control"  value="">
                </div>
                <div class="mb-3 col-md-2">
                
                <input type="date" name="one_time_income_end[]" class="form-control" value="">
            </div>
            </div>
                </div>
            `);
        });

        $('#add-expences-button').click(function() {
            $('#additional-expences-container').append(`
                <div class="additional-expences-group">
                  <div class="row">
                    <div class="mb-3 col-md-2">
                        
                        <div class="input-group">
                            <input type="text" name="additional_expences[]" class="form-control" id="additional_expences_new" value="">
                            <span class="input-group-text">$</span>
                        </div>
                    </div>
                    <div class="mb-3 col-md-6">
                       
                        <input type="text" name="additional_expences_description[]" class="form-control" id="additional_expences_description_new" value="">
                    </div>
                    <div class="mb-3 col-md-2">
                        
                        <input type="date" name="additional_iexpencesstart[]" class="form-control" id="additional_expences_start_new" value="">
                    </div>
                    <div class="mb-3 col-md-2">
                       
                        <input type="date" name="additional_expences_end[]" class="form-control" id="additional_expences_end_new" value="">
                    </div>
                    </div>
                </div>
            `);
        });
    
        $('#add-one-time-expences-button').click(function() {
            $('#one-time-expences-container').append(`
                <div class="one_time_expences-group">
                    <div class="row">
                    <div class="mb-3 col-md-2">
                        
                        <div class="input-group">
                            <input type="text" name="one_time_expences[]" class="form-control"  value="">
                            <span class="input-group-text">$</span>
                        </div>
                    </div>
                    <div class="mb-3 col-md-6">
                        
                        <input type="text" name="one_time_expences_description[]" class="form-control"  value="">
                    </div>
                    <div class="mb-3 col-md-2">
                        
                        <input type="date" name="one_time_expences_start[]" class="form-control"  value="">
                    </div>
                    <div class="mb-3 col-md-2">
                    
                    <input type="date" name="one_time_expences_end[]" class="form-control" value="">
                </div>
                </div>
                    </div>
                `);
        });
});